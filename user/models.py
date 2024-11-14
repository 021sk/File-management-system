from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='account_images/', null=True, blank=True)
    job = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

