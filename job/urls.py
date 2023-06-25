from . import views
from django.urls import path, include

app_name = "job"

urlpatterns = [
    path('', views.job_list),
    path('<id>/', views.job_detail, name='job_detail'),
]
