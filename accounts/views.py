from django.shortcuts import render


def job_list(request):
    return render(request, "accounts/job_list.html")

