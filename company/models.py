from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    location = models.CharField(max_length=200)

    website = models.URLField(blank=True)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name