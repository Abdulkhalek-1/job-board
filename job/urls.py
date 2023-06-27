from . import views
from django.urls import path, include

app_name = "job"

urlpatterns = [
    path('', views.job_list, name="jobs"),
    path('add/', views.add_job, name="add"),
    path('<id>/', views.job_detail, name='job_detail'),
]
