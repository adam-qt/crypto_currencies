from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'fadeIn second',
        'placeholder': 'Login'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'fadeIn second',
        'id': 'login',
        'placeholder': 'password',

    }))

    class Meta:
        model = User
        fields = ['username', 'password', ]


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'fadeIn second',
        'placeholder': 'username'

    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'fadeIn second',
        'placeholder': 'password'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'fadeIn second',
        'placeholder': 'confirm password'
    }))

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2')