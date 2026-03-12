from django.db import models

from accounts.models import User
from company.models import Company


class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()  # Text for TF-IDF
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    required_skills = models.ManyToManyField('skills.Skill', through='JobSkill')
    required_experience = models.IntegerField(default=0)
    status = models.CharField( max_length=20,choices=[('Open', 'Open'), ('Closed', 'Closed')],default='Open')

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=[('Applied', 'Applied'), ('Interview', 'Interview'), ('Rejected', 'Rejected'),
                                       ('Hired', 'Hired')], default='Applied')
    created_at = models.DateTimeField(auto_now_add=True)