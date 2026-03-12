# ml_engine/services.py
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
        """Fetch data from DB and convert to DataFrames"""
        # 1. Job Data (Text for Cosine)
        jobs = Job.objects.filter(status='Open')
        job_texts = [f"{j.title} {j.description}" for j in jobs]
        self.job_df = pd.DataFrame({'id': jobs.values_list('id', flat=True), 'text': job_texts})

        # 2. User Data (Skills + Bio from job_seeker)
        profiles = JobSeekerProfile.objects.select_related('user').all()
        user_data = []
        for profile in profiles:
            # Get skills as a string vector
            skills = [s.skill.name for s in profile.seekerskill_set.all()]
            text = f"{profile.bio} {' '.join(skills)}"
            user_data.append({'id': profile.user.id, 'text': text})

        self.user_df = pd.DataFrame(user_data)

    def train_cosine(self):
        """Train TF-IDF and Cosine Similarity"""
        self._prepare_data()
        self.job_vectors = self.tfidf.fit_transform(self.job_df['text'])
        self.user_vectors = self.tfidf.transform(self.user_df['text'])

    def recommend_cosine(self, user_id, top_n=5):
        """Content-Based Filtering (Job Description vs User Bio/Skills)"""
        if self.user_vectors is None:
            self.train_cosine()

        user_idx = self.user_df[self.user_df['id'] == user_id].index
        if len(user_idx) == 0:
            return []

        user_vec = self.user_vectors[user_idx]
        similarities = cosine_similarity(user_vec, self.job_vectors)[0]
        top_indices = similarities.argsort()[-top_n:][::-1]
        job_ids = self.job_df.iloc[top_indices]['id'].tolist()

        return job_ids

    def recommend_knn(self, user_id, top_n=5):
        """Collaborative Filtering (Users with similar skills)"""
        # 1. Get skills of current user
        user_skills = SeekerSkill.objects.filter(user_id=user_id).values_list('skill_id', flat=True)

        # 2. Find other users with similar skills
        similar_users = SeekerSkill.objects.filter(skill_id__in=user_skills).values_list('user_id', flat=True)
        similar_users = list(set(similar_users) - {user_id})

        # 3. Get jobs applied to by similar users
        # (Simplified logic: In production, use a User-Job matrix)
        # For now, return empty list as full implementation requires complex matrix math
        return []

    def train_classifier(self):
        """Train Naive Bayes / Decision Tree for 'Will User Apply?'"""
        # 1. Get Interaction Logs
        logs = InteractionLog.objects.filter(action='Applied')
        # 2. Create Features (Experience, Salary, Job Category, etc.)
        # 3. Fit Models
        pass

    def get_hybrid_recommendations(self, user_id, top_n=10):
        """Combine Cosine + KNN + Classifier Scores"""
        cosine_jobs = self.recommend_cosine(user_id, top_n=20)
        knn_jobs = self.recommend_knn(user_id, top_n=20)

        # Combine logic (Weighted Average)
        final_scores = {}
        for job_id in cosine_jobs:
            final_scores[job_id] = 1.0  # Placeholder weight

        # Sort by score
        sorted_jobs = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        return [job_id for job_id, score in sorted_jobs[:top_n]]