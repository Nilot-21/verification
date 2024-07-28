from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=("full_name","age","username","password1","password2")

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)