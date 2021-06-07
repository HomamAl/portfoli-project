from django.shortcuts import render, get_object_or_404
from .models import job

def home(request):
    jobs = job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    projectdetail = get_object_or_404(job, pk=job_id)    
    return render(request, 'jobs/details.html', {'job':projectdetail})