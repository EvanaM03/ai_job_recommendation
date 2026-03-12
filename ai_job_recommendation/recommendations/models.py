# recommendations/models.py
from django.db import models

from ai_job_recommendation.accounts.models import User
from ai_job_recommendation.jobs.models import Job


class InteractionLog(models.Model):
    """Tracks user behavior to train the model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    action = models.CharField(max_length=20) # 'Viewed', 'Clicked', 'Applied', 'Rejected'
    timestamp = models.DateTimeField(auto_now_add=True)

class RecommendationLog(models.Model):
    """Stores what was recommended to track accuracy"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    algorithm_used = models.CharField(max_length=50) # e.g., 'KNN', 'Cosine'
    score = models.FloatField() # Confidence score
    created_at = models.DateTimeField(auto_now_add=True)