from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', account_views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
    path('seeker/', include('job_seeker.urls')),
    path('recommendations/', include('recommendations.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)