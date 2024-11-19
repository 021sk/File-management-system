from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
                               label='password')
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
                                label='password confirmation')

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            }),

            'email': forms.TextInput(attrs={
                'class': "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
            }),

        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2:
            try:
                password_validation.validate_password(password2, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email already exists')
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250, required=True, label="username or phone",
                               widget=forms.TextInput(attrs={'class': 'forms-control'}))
    password = forms.CharField(max_length=250, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'forms-control'}))
