from django.db import models

# Create your models here.


class job(models.Model):
    title = models.CharField(max_length=75)
    discription = models.TextField()
