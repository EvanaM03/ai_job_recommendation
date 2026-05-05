
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Job, JobCategory, JobApplication
from recommendations.models import InteractionLog



def job_list(request):
    jobs = Job.objects.filter(status='Open').select_related('category', 'company')
    categories = JobCategory.objects.all()

    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    location = request.GET.get('location', '')
    job_type = request.GET.get('job_type', '')

    if query:
        jobs = jobs.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(company_name__icontains=query))
    if category_slug:
        jobs = jobs.filter(category__slug=category_slug)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
        'selected_location': location,
        'selected_job_type': job_type,
        'job_types': Job.JOB_TYPE_CHOICES,
    })


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    has_applied = False
    if request.user.is_authenticated:
        has_applied = JobApplication.objects.filter(job=job, applicant=request.user).exists()
        InteractionLog.objects.create(user=request.user, job=job, action='viewed')
    related_jobs = Job.objects.filter(status='Open', category=job.category).exclude(pk=job_id)[:4]
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied,
        'related_jobs': related_jobs,
    })


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, status='Open')
    if JobApplication.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job_detail', job_id=job_id)
    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter', '')
        JobApplication.objects.create(job=job, applicant=request.user, cover_letter=cover_letter)
        InteractionLog.objects.create(user=request.user, job=job, action='applied')
        messages.success(request, f'Successfully applied for "{job.title}"!')
        return redirect('dashboard')
    return render(request, 'jobs/apply.html', {'job': job})


@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(applicant=request.user).select_related('job').order_by('-applied_at')

    return render(request, 'jobs/my_applications.html', {'applications': applications})

