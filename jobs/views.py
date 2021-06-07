from django.shortcuts import get_object_or_404, render
from .models import job

def home(request):
    jobs = job.objects
    return render(request, 'jobs/home.html', {'job':job})

def details(request, jobs_id):
    jobsdetail = get_object_or_404(job, pk=jobs_id)    
    return render(request, 'jobs/detail.html', {'jobs':jobsdetail})