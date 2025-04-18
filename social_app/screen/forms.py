from django import forms 
from .models import Screen
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

