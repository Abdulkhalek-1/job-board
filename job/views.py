from django.db.models import F
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import job
from .forms import ApplyForm, jobForm


def job_list(request):
    job_list = job.objects.order_by(F("published_at").desc())
    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj, "count": job_list.count}
    return render(request, "job/job_list.html", context)


def job_detail(request, id):
    try:
        job_detail = job.objects.get(id=id)
        if request.method == "POST":
            form = ApplyForm(request.POST, request.FILES)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.job = job_detail
                myform.save()
        else:
            form = ApplyForm()
        context = {"job": job_detail, "form": form}
        return render(request, "job/job_detail.html", context)
    except:
        return render(request, "job/job_detail.html", {"job.is_active": False})


def add_job(request):
    if request.method=="POST":
        form = jobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform = form.save()
    else:
        form = jobForm()
    return render(request, 'job/add_job.html', {"form": form})
