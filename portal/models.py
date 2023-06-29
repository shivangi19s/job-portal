from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class JobPosting(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    why = models.TextField()


