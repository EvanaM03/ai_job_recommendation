# AI Job Recommendation System

## Overview
A Django-based job recommendation web application that uses machine learning to match job seekers with relevant job postings.

## Tech Stack
- **Backend**: Django 6.0.3 (Python 3.12)
- **Database**: SQLite (local development)
- **ML Libraries**: scikit-learn, pandas, numpy
- **Production Server**: Gunicorn

## Project Structure
- `ai_job_recommendation/` - Django project settings, URLs, WSGI/ASGI config
- `accounts/` - Custom user model (extends AbstractUser)
- `job_seeker/` - Job seeker profiles, resumes, skills
- `company/` - Company profiles
- `jobs/` - Job postings, categories, required skills
- `skill/` - Master skill list
- `ml_engine/` - ML recommendation engine (TF-IDF, Cosine Similarity, KNN)
- `recommendations/` - User interaction logs and recommendation scores
- `dataset/` - Dataset management

## ML Features
- Content-Based Filtering using TF-IDF Vectorization and Cosine Similarity
- Collaborative Filtering via KNN (partial implementation)
- Interaction tracking (views, clicks, applications)
- Hybrid recommendation system

## Setup Notes
- Originally configured for MySQL; switched to SQLite for Replit compatibility
- `ALLOWED_HOSTS = ['*']` set for Replit proxy compatibility
- Static files directory: `static/`
- Media files directory: `media/`

## Running
- Development: `python manage.py runserver 0.0.0.0:5000`
- Production: `gunicorn --bind=0.0.0.0:5000 --reuse-port ai_job_recommendation.wsgi:application`

## Admin
Access the Django admin at `/admin/`
