# AI Job Recommendation System (JobAI)

## Overview
A full-stack Django web application with an AI-powered job recommendation engine that matches job seekers with relevant positions using machine learning.

## Tech Stack
- **Backend**: Django 6.0.3 (Python 3.12)
- **Database**: SQLite (local development)
- **ML Libraries**: scikit-learn (TF-IDF, Cosine Similarity, KNN), pandas, numpy
- **Image Processing**: Pillow
- **Frontend**: Tailwind CSS (CDN), Font Awesome icons
- **Production Server**: Gunicorn

## Features Built
- **Authentication**: Register, Login, Logout with custom User model
- **Job Browsing**: Search, filter by category/location/type, paginated cards
- **Job Detail**: Full job view with apply button and related jobs
- **Job Application**: Cover letter submission, application tracking
- **Job Seeker Profile**: Bio, career objective, resume upload, profile picture
- **Skills Management**: Add/remove skills with proficiency levels (AI-matched)
- **Education History**: Add/remove education records
- **Work Experience**: Add/remove work history
- **AI Recommendations**: TF-IDF + Cosine Similarity matching engine
- **Dashboard**: Quick stats, recent applications, activity log
- **Admin Panel**: Full Django admin for all models

## Project Structure
- `accounts/` - Custom User model, UserProfile, auth views (login/register/dashboard)
- `job_seeker/` - JobSeekerProfile, SeekerSkill, Education, WorkExperience
- `company/` - Company model and admin
- `jobs/` - Job, JobCategory, JobApplication models and views
- `skill/` - Master Skill list (42 pre-seeded skills)
- `ml_engine/` - JobRecommender class (TF-IDF, Cosine, KNN, Naive Bayes)
- `recommendations/` - InteractionLog, RecommendationLog, recommendation views
- `dataset/` - ML training dataset model
- `templates/` - All HTML templates using Tailwind CSS

## URL Routes
- `/` - Home page
- `/accounts/register/` - Registration
- `/accounts/login/` - Login
- `/accounts/dashboard/` - User dashboard
- `/jobs/` - Job listings (search + filter)
- `/jobs/<id>/` - Job detail
- `/jobs/<id>/apply/` - Apply for a job
- `/jobs/my-applications/` - Application tracker
- `/seeker/setup/` - Profile setup wizard
- `/seeker/profile/` - View profile
- `/seeker/profile/edit/` - Edit profile
- `/seeker/profile/skills/` - Manage skills
- `/seeker/profile/education/` - Manage education
- `/seeker/profile/experience/` - Manage work experience
- `/recommendations/` - AI job recommendations
- `/admin/` - Django admin panel

## Seed Data
42 skills, 8 job categories, 5 companies, 12 sample jobs seeded via:
```
python manage.py seed_data
```

## Admin Access
- Username: `admin`
- Password: `admin123`
- URL: `/admin/`

## Running
- Development: `python manage.py runserver 0.0.0.0:5000`
- Production: `gunicorn --bind=0.0.0.0:5000 --reuse-port ai_job_recommendation.wsgi:application`

## ML Algorithm
The AI recommendation uses:
1. **TF-IDF Vectorization** — converts job descriptions and user bio+skills into numeric vectors
2. **Cosine Similarity** — measures how similar a user's profile is to each job
3. Jobs with highest similarity scores are recommended first
