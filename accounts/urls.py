from . import views
from django.urls import path

urlpatterns = [
    path('signup', views.signu, name="signup"),
]
