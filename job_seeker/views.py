from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobSeekerProfile, SeekerSkill, Education, WorkExperience
from .forms import JobSeekerProfileForm, SeekerSkillForm, EducationForm, WorkExperienceForm


@login_required
def setup_profile(request):
    profile, created = JobSeekerProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = JobSeekerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile saved! Now add your skills.')
            return redirect('manage_skills')
    else:
        form = JobSeekerProfileForm(instance=profile)
    return render(request, 'job_seeker/setup_profile.html', {'form': form, 'created': created})


@login_required
def profile_view(request):
    try:
        profile = request.user.jobseekerprofile
    except JobSeekerProfile.DoesNotExist:
        return redirect('setup_profile')
    skills = profile.seekerskill_set.select_related('skill').all()
    education = profile.education_set.all()
    experience = profile.workexperience_set.all().order_by('-start_date')
    return render(request, 'job_seeker/profile.html', {
        'profile': profile,
        'skills': skills,
        'education': education,
        'experience': experience,
    })


@login_required
def edit_profile(request):
    profile, _ = JobSeekerProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = JobSeekerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_view')
    else:
        form = JobSeekerProfileForm(instance=profile)
    return render(request, 'job_seeker/edit_profile.html', {'form': form})


@login_required
def manage_skills(request):
    profile, _ = JobSeekerProfile.objects.get_or_create(user=request.user)
    skills = profile.seekerskill_set.select_related('skill').all()
    if request.method == 'POST':
        form = SeekerSkillForm(request.POST)
        if form.is_valid():
            skill = form.cleaned_data['skill']
            if SeekerSkill.objects.filter(job_seeker=profile, skill=skill).exists():
                messages.warning(request, f'"{skill.name}" is already in your skills.')
            else:
                seeker_skill = form.save(commit=False)
                seeker_skill.job_seeker = profile
                seeker_skill.save()
                messages.success(request, f'"{skill.name}" added to your skills!')
            return redirect('manage_skills')
    else:
        form = SeekerSkillForm()
    return render(request, 'job_seeker/manage_skills.html', {'form': form, 'skills': skills})


@login_required
def delete_skill(request, skill_id):
    profile = get_object_or_404(JobSeekerProfile, user=request.user)
    skill = get_object_or_404(SeekerSkill, pk=skill_id, job_seeker=profile)
    skill.delete()
    messages.success(request, 'Skill removed.')
    return redirect('manage_skills')


@login_required
def manage_education(request):
    profile, _ = JobSeekerProfile.objects.get_or_create(user=request.user)
    education_list = profile.education_set.all()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.job_seeker = profile
            edu.save()
            messages.success(request, 'Education record added!')
            return redirect('manage_education')
    else:
        form = EducationForm()
    return render(request, 'job_seeker/manage_education.html', {'form': form, 'education_list': education_list})


@login_required
def delete_education(request, edu_id):
    profile = get_object_or_404(JobSeekerProfile, user=request.user)
    edu = get_object_or_404(Education, pk=edu_id, job_seeker=profile)
    edu.delete()
    messages.success(request, 'Education record removed.')
    return redirect('manage_education')


@login_required
def manage_experience(request):
    profile, _ = JobSeekerProfile.objects.get_or_create(user=request.user)
    experience_list = profile.workexperience_set.all().order_by('-start_date')
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.job_seeker = profile
            exp.save()
            messages.success(request, 'Work experience added!')
            return redirect('manage_experience')
    else:
        form = WorkExperienceForm()
    return render(request, 'job_seeker/manage_experience.html', {'form': form, 'experience_list': experience_list})


@login_required
def delete_experience(request, exp_id):
    profile = get_object_or_404(JobSeekerProfile, user=request.user)
    exp = get_object_or_404(WorkExperience, pk=exp_id, job_seeker=profile)
    exp.delete()
    messages.success(request, 'Work experience removed.')
    return redirect('manage_experience')
