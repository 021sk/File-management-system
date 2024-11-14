from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sub_folders')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class File(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE, related_name='files')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    size = models.PositiveIntegerField()  # In bytes

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
