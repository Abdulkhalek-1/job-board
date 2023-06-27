from django.shortcuts import render
from .models import job

def index(request):
    jobs = job.objects.all()
    context = {"jobs": jobs}
    return render(request, "home/index.html", context)
