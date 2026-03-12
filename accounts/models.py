from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mobile = models.CharField(max_length=255, blank=True)
    # Remove address here, put in profile for better separation


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Experience & Education
    experience_years = models.IntegerField(default=0)
    education_level = models.CharField(max_length=50, default='Bachelor')
    location = models.CharField(max_length=100)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Text for Cosine Similarity
    bio = models.TextField(blank=True, help_text="Summary of skills and goals")

    # Preferences for Filtering
    remote_preference = models.BooleanField(default=False)
    preferred_locations = models.JSONField(default=list, blank=True)  # e.g. ["New York", "Remote"]

    def __str__(self):
        return f"{self.user.username} Profile"


