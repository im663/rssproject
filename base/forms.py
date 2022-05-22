from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Settings


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
