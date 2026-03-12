from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import JobSeekerProfile, SeekerSkill, Application
from jobs.models import Job
from recommendation.models import InteractionLog
from ml_engine.services import JobRecommender

recommender = JobRecommender()


@login_required
def profile_update(request):
    """Update Bio, Skills, Experience"""
    profile, created = JobSeekerProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.bio = request.POST.get('bio')
        profile.experience_years = request.POST.get('experience_years')
        profile.location = request.POST.get('location')
        profile.save()

        # Update Skills
        skill_ids = request.POST.getlist('skills')
        SeekerSkill.objects.filter(user=request.user).delete()
        for skill_id in skill_ids:
            SeekerSkill.objects.create(
                user=request.user,
                skill_id=skill_id,
                proficiency=3,  # Default proficiency
                years_used=0
            )
        return redirect('job_seeker:profile')

    return render(request, 'job_seeker/profile.html', {'profile': profile})


@login_required
@require_http_methods(["POST"])
def apply_job(request):
    """Handle Job Application & Log Interaction"""
    job_id = request.POST.get('job_id')
    job = get_object_or_404(Job, id=job_id)

    # Create Application
    Application.objects.create(user=request.user, job=job)

    # Log Interaction for ML Training
    InteractionLog.objects.create(
        user=request.user,
        job=job,
        action='Applied'
    )

    return JsonResponse({'status': 'Applied'})


@login_required
@require_http_methods(["GET"])
def get_recommendations(request):
    """Fetch AI Recommendations"""
    user_id = request.user.id

    # Initialize and Train if needed
    if recommender.user_vectors is None:
        recommender.train_cosine()

    job_ids = recommender.get_hybrid_recommendations(user_id, top_n=10)

    # Fetch Job Details
    jobs = Job.objects.filter(id__in=job_ids)

    # Log the recommendation
    for job in jobs:
        InteractionLog.objects.create(
            user=request.user,
            job=job,
            action='Viewed'
        )

    data = [
        {
            'id': job.id,
            'title': job.title,
            'company': job.company_name,
            'location': job.location
        } for job in jobs
    ]

    return JsonResponse({'recommendations': data})