from django.db import models
from django.utils.text import slugify

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
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=r"jobs/%d-%m-%Y", blank=True, null=True, default="jobs/1.svg")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(job, related_name="apply_job", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField()
    created_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name
