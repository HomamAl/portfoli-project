from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/<int:jobs_id>/', views.details, name='details'),
] 
