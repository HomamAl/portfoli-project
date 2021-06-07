from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:jobs_id>/', views.detail, name='detail'),
] 
