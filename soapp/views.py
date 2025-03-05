from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def main(request):

    posts = Post.objects.order_by('-created_at')

    return render(request, 'soapp/main.html', {'posts': posts})


def main_author(request, author_id):

    posts = Post.objects.filter(author=author_id).order_by('-created_at')

    return render(request, 'soapp/main.html', {'posts': posts})


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

    posts = Post.objects.filter(author=request.user.id)
    if request.method == 'POST':
        avatar_form = ProfileAvatarUpdate(request.POST, request.FILES, instance=request.user.profile)
        profile_form = ProfileEdit(request.POST, request.FILES, instance=request.user)
        if avatar_form.is_valid():
            avatar_form.save()
        if profile_form.is_valid():
            user_edit = request.user
            user_edit.username = request.POST.get('username')
            user_edit.first_name = request.POST.get('first_name')
            user_edit.email = request.POST.get('email')
            user_edit.save()

        return redirect('profile')
    else:
        avatar_form = ProfileAvatarUpdate(instance=request.user.profile)
        profile_form = ProfileEdit(instance=request.user)

    context = {'avatar_form': avatar_form, 'profile_form': profile_form, 'posts': posts}
    return render(request, 'soapp/profile.html', context)


def profile_view(request, username):

    user = User.objects.get(username=username)
    profile_obj = Profile.objects.get(user=user)
    posts = Post.objects.filter(author=user.id)

    context = {'posts': posts, 'profile_obj': profile_obj}
    return render(request, 'soapp/another_profile.html', context)


def logout_url(request):
    logout(request)
    return redirect('/')


@login_required
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post_obj = Post()
        post_obj.author = User.objects.get(username=request.user.username)
        post_obj.image = request.FILES.get('image')
        post_obj.description = request.POST.get('description')
        post_obj.save()

        return redirect('/')

    else:
        form = PostForm()

    return render(request, 'soapp/post_create.html', {'form': form})


def post(request, post_id):

    post_obj = Post.objects.get(id=post_id)

    return render(request, 'soapp/post.html', {'post': post_obj})


def post_delete(request, post_id):

    post_obj = Post.objects.get(id=post_id)
    post_obj.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def like_post(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    if request.user in post_obj.likes.all():
        post_obj.likes.remove(request.user)
    else:
        post_obj.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))
