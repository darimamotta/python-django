from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import Allcourses, details, Tag, Post, Login
admin.site.register(Allcourses)
admin.site.register(details)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Login)


