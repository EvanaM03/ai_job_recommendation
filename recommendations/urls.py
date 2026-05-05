from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommendations_view, name='recommendations'),
    path('api/<int:user_id>/', views.get_recommendations_api, name='recommendations_api'),
]
