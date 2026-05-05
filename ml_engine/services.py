import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from accounts.models import User
from job_seeker.models import JobSeekerProfile, SeekerSkill
from jobs.models import Job
from recommendations.models import InteractionLog


class JobRecommender:
    def __init__(self):
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.knn = NearestNeighbors(n_neighbors=5)
        self.naive_bayes = MultinomialNB()
        self.decision_tree = DecisionTreeClassifier()
        self.job_vectors = None
        self.user_vectors = None
        self.job_df = None
        self.user_df = None

    def _prepare_data(self):
        # Materialize jobs into a list once with a stable ordering
        # to prevent ID/text misalignment from double queryset evaluation
        jobs = list(Job.objects.filter(status='Open').order_by('id'))
        job_ids = [j.id for j in jobs]
        job_texts = [f"{j.title} {j.description}" for j in jobs]
        self.job_df = pd.DataFrame({'id': job_ids, 'text': job_texts})

        # User profiles with skills
        profiles = (
            JobSeekerProfile.objects
            .select_related('user')
            .prefetch_related('seekerskill_set__skill')
            .all()
        )
        user_data = []
        for profile in profiles:
            skills = [s.skill.name for s in profile.seekerskill_set.all()]
            text = f"{profile.bio or ''} {' '.join(skills)}"
            user_data.append({'id': profile.user.id, 'text': text})

        self.user_df = pd.DataFrame(user_data) if user_data else pd.DataFrame(columns=['id', 'text'])

    def train_cosine(self):
        self._prepare_data()
        if self.job_df.empty or self.user_df.empty:
            return
        self.job_vectors = self.tfidf.fit_transform(self.job_df['text'])
        self.user_vectors = self.tfidf.transform(self.user_df['text'])

    def recommend_cosine(self, user_id, top_n=10):
        """Return list of Job IDs ranked by cosine similarity to the user profile."""
        self.train_cosine()

        if self.job_vectors is None or self.user_df.empty:
            return []

        user_idx = self.user_df[self.user_df['id'] == user_id].index
        if len(user_idx) == 0:
            return []

        user_vec = self.user_vectors[user_idx]
        similarities = cosine_similarity(user_vec, self.job_vectors)[0]
        top_indices = similarities.argsort()[-top_n:][::-1]
        job_ids = self.job_df.iloc[top_indices]['id'].tolist()
        return job_ids

    def recommend_knn(self, user_id, top_n=5):
        user_skills = SeekerSkill.objects.filter(user_id=user_id).values_list('skill_id', flat=True)
        similar_users = SeekerSkill.objects.filter(skill_id__in=user_skills).values_list('user_id', flat=True)
        similar_users = list(set(similar_users) - {user_id})
        return []

    def train_classifier(self):
        pass

    def get_hybrid_recommendations(self, user_id, top_n=10):
        cosine_jobs = self.recommend_cosine(user_id, top_n=20)
        final_scores = {job_id: 1.0 for job_id in cosine_jobs}
        sorted_jobs = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        return [job_id for job_id, score in sorted_jobs[:top_n]]
