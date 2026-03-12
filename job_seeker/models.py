from django.db import models
from django.contrib.auth import get_user_model

from skill.models import Skill

User = get_user_model()


class JobSeekerProfile(models.Model):
    """Extends the User model with job-seeking specific data"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seeker_profile')

    # Text for Cosine Similarity
    bio = models.TextField(blank=True, help_text="Summary of skills and goals")

    # Features for Decision Tree / Naive Bayes
    experience_years = models.IntegerField(default=0)
    education_level = models.CharField(max_length=50, default='Bachelor')
    location = models.CharField(max_length=100)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Preferences for Filtering
    remote_preference = models.BooleanField(default=False)
    preferred_locations = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class SeekerSkill(models.Model):
    """Links User to Skills (Replaces UserSkill in accounts)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seeker_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')])
    years_used = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'skill')


class Application(models.Model):
    """Tracks applications made by the seeker"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Applied')  # Applied, Interview, Rejected
    created_at = models.DateTimeField(auto_now_add=True)

    # Add this for ML Training (Did they actually get the job?)
    is_hired = models.BooleanField(default=False)