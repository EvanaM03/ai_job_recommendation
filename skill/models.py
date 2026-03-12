from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50) # e.g., 'Programming', 'Soft Skill'
    description = models.TextField(blank=True) # For better TF-IDF matching

    def __str__(self):
        return self.name

class JobSkill(models.Model):
    """Link between Job and Skills"""
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='job_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    is_required = models.BooleanField(default=True) # Required vs Preferred

    class Meta:
        unique_together = ('job', 'skill')