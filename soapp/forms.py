from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CreateUser(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


class ProfileAvatarUpdate(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ['image']


class ProfileEdit(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'first_name', 'email']

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ['image', 'description']
