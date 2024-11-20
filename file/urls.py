from django.urls import path
from . import views

app_name = 'file'
urlpatterns = [
    path('', views.dashboard, name='home')

]
