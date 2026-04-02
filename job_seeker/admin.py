from django.contrib import admin
from .models import JobSeekerProfile, SeekerSkill, Education, WorkExperience


class SeekerSkillInline(admin.TabularInline):
    model = SeekerSkill
    extra = 0


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0


class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 0


@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'current_location', 'expected_salary', 'created_at']
    search_fields = ['user__username', 'current_location']
    inlines = [SeekerSkillInline, EducationInline, WorkExperienceInline]


@admin.register(SeekerSkill)
class SeekerSkillAdmin(admin.ModelAdmin):
    list_display = ['job_seeker', 'skill', 'proficiency']
    list_filter = ['proficiency']
