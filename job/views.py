from django.shortcuts import render
from django.core.paginator import Paginator
from .models import job


def job_list(request):
    job_list = job.objects.all()
    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj,
                "count": job_list.count
                }
    return render(request, "job/job_list.html", context)


def job_detail(request, id):
    try:
        job_detail = job.objects.get(id=id)
        context = {"job": job_detail}
        return render(request, "job/job_detail.html", context)
    except:
        return render(request, "job/job_detail.html", {"job.is_active": False})
