from django.contrib import admin
from .models import InteractionLog, RecommendationLog
# Register your models here.

@admin.register(InteractionLog)
class InteractionLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'action', 'timestamp']
    list_filter = ['action']


@admin.register(RecommendationLog)
class RecommendationLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'algorithm_used', 'score', 'created_at']
    list_filter = ['algorithm_used']