from django.shortcuts import render, get_object_or_404
from .models import job

def home(request):
    jobs = job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def details(request, job_id):
    detailjobs = get_object_or_404(job, pk=job_id)    
    return render(request, 'jobs/info.html', {'job':detailjobs})