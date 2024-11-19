from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'photo', 'job', 'phone_number')}),

    )
