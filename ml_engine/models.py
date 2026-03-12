from django.db import models

from accounts.models import User
from jobs.models import Job


class CachedRecommendation(models.Model):

    ALGORITHMS = [
        ('cosine','Cosine Similarity'),
        ('knn','KNN'),
        ('naive_bayes','Naive Bayes'),
        ('decision_tree','Decision Tree')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    score = models.FloatField()

    algorithm = models.CharField(max_length=50, choices=ALGORITHMS)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')