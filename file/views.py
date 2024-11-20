from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Folder, File


@login_required
def dashboard(request):
    folders = Folder.objects.filter(owner=request.user, parent=None)
    root_folders = Folder.objects.get(owner=request.user, parent=None)
    return render(request, 'dashboard.html', {'folders': folders, 'root_folders': root_folders})
