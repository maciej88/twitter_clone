from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea
from .models import *

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=64, label='Login (email)')
    password = forms.CharField(max_length=64, label="Password", widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=64, label='Email as Login', help_text='Required. Enter a valid email adress.')

    class Meta:
        user = User
        fields = ('email', 'password1', 'password2')

