from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm, UserProfileForm
from .models import UserProfile
from jobs.models import Job, JobApplication
from recommendations.models import InteractionLog

def home(request):
    recent_jobs = Job.objects.filter(status='Open').order_by('-posted_date')[:6]
    total_jobs = Job.objects.filter(status='Open').count()
    return render(request, 'home.html', {'recent_jobs': recent_jobs, 'total_jobs': total_jobs})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user, defaults={'location': ''})
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}! Your account has been created.')
            return redirect('setup_profile')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect(request.GET.get('next', 'dashboard'))
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(applicant=request.user).select_related('job').order_by('-applied_at')[:5]
    recent_interactions = InteractionLog.objects.filter(user=request.user).select_related('job').order_by('-timestamp')[:5]
    try:
        profile = request.user.jobseekerprofile
        has_profile = True
    except Exception:
        has_profile = False
        profile = None
    return render(request, 'accounts/dashboard.html', {
        'applications': applications,
        'recent_interactions': recent_interactions,
        'has_profile': has_profile,
        'profile': profile,
    })