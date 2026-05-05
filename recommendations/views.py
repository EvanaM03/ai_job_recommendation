
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ml_engine.services import JobRecommender
from jobs.models import Job
from .models import InteractionLog, RecommendationLog


@login_required
def recommendations_view(request):
    user = request.user
    recommended_jobs = []
    error_message = None


    try:
        # Always clear stale recommendation logs so deleted jobs never resurface
        RecommendationLog.objects.filter(user=user).delete()

        recommender = JobRecommender()
        job_ids = recommender.recommend_cosine(user.id, top_n=10)

        if job_ids:
            # Preserve the ML-ranked order
            jobs_by_id = {
                j.id: j
                for j in Job.objects.filter(id__in=job_ids, status='Open').select_related('category', 'company')
            }
            recommended_jobs = [jobs_by_id[jid] for jid in job_ids if jid in jobs_by_id]

            for job in recommended_jobs:
                RecommendationLog.objects.create(
                    user=user, job=job, algorithm_used='cosine', score=1.0
                )
        else:
            error_message = (
                "No recommendations yet. Complete your profile and add skills "
                "to get personalized recommendations!"
            )
    except Exception as e:
        error_message = "Could not generate recommendations. Make sure your profile and skills are complete."

    recent_interactions = (
        InteractionLog.objects
        .filter(user=user)
        .select_related('job')
        .order_by('-timestamp')[:5]
    )


    return render(request, 'recommendations/recommendations.html', {
        'recommended_jobs': recommended_jobs,
        'error_message': error_message,
        'recent_interactions': recent_interactions,
    })


def get_recommendations_api(request, user_id):
    recommender = JobRecommender()
    jobs = recommender.recommend_cosine(user_id, top_n=5)
    return JsonResponse({'jobs': jobs})
