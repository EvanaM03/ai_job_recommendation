from django.urls import path
from . import views

urlpatterns = [
    path('setup/', views.setup_profile, name='setup_profile'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/skills/', views.manage_skills, name='manage_skills'),
    path('profile/skills/delete/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('profile/education/', views.manage_education, name='manage_education'),
    path('profile/education/delete/<int:edu_id>/', views.delete_education, name='delete_education'),
    path('profile/experience/', views.manage_experience, name='manage_experience'),
    path('profile/experience/delete/<int:exp_id>/', views.delete_experience, name='delete_experience'),
]
