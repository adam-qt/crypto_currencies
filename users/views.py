from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm, UserLoginForm
from django.urls import  reverse_lazy
from django.contrib.auth.views import LoginView


class UserRegistrationView( CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserLoginView( LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


