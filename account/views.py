from django.views.generic import View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView as _LoginView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


class RegisterView(CreateView, SuccessMessageMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('file:home')
        return super().dispatch(request, *args, **kwargs)

    template_name = "account/registration.html"
    # model = User
    form_class = UserRegistrationForm
    success_message = "Your profile was created successfully"
    success_url = reverse_lazy("file:home")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, "Registration Successful")

        return super().form_valid(form)


class LoginView(_LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('file:home')
        return super().dispatch(request, *args, **kwargs)

    redirect_authenticated_user = True
    next_page = "file:home"
    template_name = "account/login.html"
    authentication_form = LoginForm


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('user:login')
