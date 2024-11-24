from django.urls import path
from . import views


app_name = 'file'
urlpatterns = [
    # view
    path('', views.DashboardView.as_view(), name='home'),
    path('/folder/<int:folder_id>/', views.FolderDetailView.as_view(), name='folder_detail'),

]+[
    # api_view

]

