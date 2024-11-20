from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from .models import Folder, File


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all root-level folders and files for the authenticated user
        context['folders'] = Folder.objects.filter(owner=self.request.user, parent=None)
        context['files'] = File.objects.filter(owner=self.request.user, folder=None)
        return context


class FolderDetailView(LoginRequiredMixin, View):
    detail_template = 'folder_detail.html'

    def get(self, request, folder_id):
        folder = get_object_or_404(Folder, id=folder_id, owner=request.user)
        sub_folders = folder.sub_folders.all()
        files = folder.files.all()
        return render(request, self.detail_template, {'folder': folder, 'sub_folders': sub_folders, 'files': files})
