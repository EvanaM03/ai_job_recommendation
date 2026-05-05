from django.contrib import admin
from .models import Job, JobCategory, JobApplication
# Register your models here.

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'location', 'job_type', 'status', 'posted_date']
    list_filter = ['status', 'job_type', 'category']
    search_fields = ['title', 'company_name', 'description']
    filter_horizontal = ['required_skills']


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'applied_at']
    list_filter = ['status']
    search_fields = ['applicant__username', 'job__title']