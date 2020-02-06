from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # gives us a nested spot to configure the model that's affected and where the info is saved to...and in what order
        model = User
        fields = ['username', 'email', 'password1', 'password2']
