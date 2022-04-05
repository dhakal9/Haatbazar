from email.policy import default
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.IntegerField()
    dob = forms.DateField()
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone', 'dob', 'username',  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.IntegerField()
    dob = forms.DateField()
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone', 'dob', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
