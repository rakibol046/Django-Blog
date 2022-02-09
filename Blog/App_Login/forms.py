from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from App_Login.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserChange(UserChangeForm):
    class Meta():
        model = User
        fields = ('email', 'first_name', 'last_name')


class UpdateProfilePic(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['profile_pic', ]

