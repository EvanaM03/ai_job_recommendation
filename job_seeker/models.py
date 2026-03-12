from django.db import models
from accounts.models import User
from skill.models import Skill


class JobSeekerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              blank=True)
    current_location = models.CharField(max_length=200)
    preferred_job_location = models.CharField(max_length=200)
    expected_salary = models.IntegerField(null=True, blank=True)
    career_objective = models.TextField(blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


class Education(models.Model):
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.degree


class WorkExperience(models.Model):
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.position


class PreferredJobCategory(models.Model):
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class SkillVector(models.Model):
    job_seeker = models.OneToOneField(JobSeekerProfile, on_delete=models.CASCADE)
    vector_data = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)