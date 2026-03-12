from django.db import models
from accounts.models import User
from jobs.models import Job


class TrainingDataset(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    label = models.IntegerField()
    # 1 = good recommendation
    # 0 = bad recommendation

    created_at = models.DateTimeField(auto_now_add=True)