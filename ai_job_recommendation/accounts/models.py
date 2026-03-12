# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add specific user data for ML
    experience_years = models.IntegerField(default=0)
    education_level = models.CharField(max_length=50) # e.g., Bachelor, Master
    location = models.CharField(max_length=100)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField(blank=True) # Text for Cosine Similarity

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50) # e.g., 'Programming', 'Soft Skill'

    def __str__(self):
        return self.name

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')])
    years_used = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'skill')