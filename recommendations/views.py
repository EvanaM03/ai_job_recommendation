# recommendations/views.py (Final Step)
from django.http import JsonResponse

from ml_engine.services import JobRecommender


def get_recommendations(request, user_id):
    recommender = JobRecommender()
    # Now you call the method you tested in test_ml.py
    jobs = recommender.recommend_cosine(user_id, top_n=5)
    return JsonResponse({'jobs': jobs})