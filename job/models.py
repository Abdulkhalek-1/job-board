from django.db import models

# Create your models here.

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)


class job(models.Model):
    title = models.CharField(max_length=75)
    #! location
    jobtype = models.CharField(choices=JOB_TYPE, max_length=50)
    discription = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
