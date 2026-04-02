from django import forms
from .models import JobSeekerProfile, SeekerSkill, Education, WorkExperience
from skill.models import Skill


INPUT_CLASS = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
TEXTAREA_CLASS = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['date_of_birth', 'gender', 'current_location', 'preferred_job_location',
                  'expected_salary', 'career_objective', 'bio', 'resume', 'profile_picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASS}),
            'gender': forms.Select(attrs={'class': INPUT_CLASS}),
            'current_location': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'e.g. New York, NY'}),
            'preferred_job_location': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'e.g. Remote or San Francisco'}),
            'expected_salary': forms.NumberInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Annual salary in USD'}),
            'career_objective': forms.Textarea(attrs={'rows': 3, 'class': TEXTAREA_CLASS}),
            'bio': forms.Textarea(attrs={'rows': 5, 'class': TEXTAREA_CLASS, 'placeholder': 'Describe your skills, experience, and goals...'}),
            'resume': forms.FileInput(attrs={'class': 'w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100'}),
            'profile_picture': forms.FileInput(attrs={'class': 'w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100'}),
        }


class SeekerSkillForm(forms.ModelForm):
    skill = forms.ModelChoiceField(
        queryset=Skill.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': INPUT_CLASS})
    )

    class Meta:
        model = SeekerSkill
        fields = ['skill', 'proficiency']
        widgets = {
            'proficiency': forms.Select(attrs={'class': INPUT_CLASS}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'field_of_study', 'graduation_year']
        widgets = {
            'degree': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'e.g. Bachelor of Science'}),
            'institution': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'University or College name'}),
            'field_of_study': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'e.g. Computer Science'}),
            'graduation_year': forms.NumberInput(attrs={'class': INPUT_CLASS, 'placeholder': 'e.g. 2022'}),
        }


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company_name', 'position', 'start_date', 'end_date', 'description', 'is_current']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'position': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASS}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': TEXTAREA_CLASS}),
            'is_current': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-indigo-600'}),
        }
