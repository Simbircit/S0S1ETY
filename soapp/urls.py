from django.contrib.auth.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns =[
    path('', views.main, name='S0S1ETY'),
    path('login/', auth_views.LoginView.as_view(), name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_url, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_profile/<str:username>', views.create_profile, name='create_profile'),
    path('password_change_form/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change_form'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done')
]
