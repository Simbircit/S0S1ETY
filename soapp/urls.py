from django.contrib.auth.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.main, name='S0S1ETY'),
    path('author/<int:author_id>/', views.main_author, name='author'),
    path('login/', auth_views.LoginView.as_view(), name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_url, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post_create/', views.create_post, name='post_create'),
    path('post/<post_id>/', views.post, name='post'),
    path('post_delete/<post_id>', views.post_delete, name='post_delete'),
    path('like/<post_id>/', views.like_post, name='like_post'),
    path('profile/<str:username>', views.profile_view, name='another_profile'),
    path('create_profile/<str:username>', views.create_profile, name='create_profile'),
    path('password_change_form/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change_form'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done')
]
