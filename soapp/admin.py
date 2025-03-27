from django.contrib import admin
from .models import *
from shapp.models import *
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Product)
