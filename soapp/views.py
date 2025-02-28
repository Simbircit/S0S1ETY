from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def main(request):

    return render(request, 'soapp/main.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect(f'/create_profile/{username}', {form.cleaned_data['username']})
    else:
        form = UserCreationForm

    return render(request, 'soapp/register.html', {'form': form})


def create_profile(request, username):
    profile_obj = Profile()
    profile_obj.user = User.objects.get(username=username)
    profile_obj.save()
    return render(request, 'soapp/main.html')


@login_required
def profile(request):
    if request.method == 'POST':
        avatar_form = ProfileAvatarUpdate(request.POST, request.FILES, instance=request.user.profile)
        if avatar_form.is_valid():
            avatar_form.save()
        return redirect('profile')
    else:
        avatar_form = ProfileAvatarUpdate(instance=request.user.profile)

    context = {'avatar_form': avatar_form}
    return render(request, 'soapp/profile.html', context)


def logout_url(request):
    logout(request)
    return redirect('/')
