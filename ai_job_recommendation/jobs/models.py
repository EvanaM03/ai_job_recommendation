# jobs/models.py
from django.db import models

from ai_job_recommendation.accounts.models import User, Skill


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() # Text for TF-IDF / Cosine Similarity
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Open') # Open, Closed

    # Many-to-Many for Skills
    required_skills = models.ManyToManyField(Skill, related_name='jobs')
    required_experience = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Applied') # Applied, Interview, Rejected
    created_at = models.DateTimeField(auto_now_add=True)