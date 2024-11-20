from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class FileInline(admin.StackedInline):
    model = File


@admin.register(Folder)
class FileAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'owner']
    inlines = [FileInline]
