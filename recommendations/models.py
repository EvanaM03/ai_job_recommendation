from django.db import models
from accounts.models import User
from jobs.models import Job


class InteractionLog(models.Model):

    ACTIONS = [
        ('viewed','Viewed'),
        ('clicked','Clicked'),
        ('applied','Applied'),
        ('rejected','Rejected')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    action = models.CharField(max_length=20, choices=ACTIONS)

    timestamp = models.DateTimeField(auto_now_add=True)


class RecommendationLog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    algorithm_used = models.CharField(max_length=50)

    score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)