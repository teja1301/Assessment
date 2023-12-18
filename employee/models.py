from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15, blank=True)
    address_details = models.JSONField()
    work_experience = models.JSONField()
    qualifications = models.JSONField()
    projects = models.JSONField()
    photo = models.TextField(blank=True)
