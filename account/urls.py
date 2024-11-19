from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('logout/', views.UserLogoutView.as_view(), name='logout' ),
    path('', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
