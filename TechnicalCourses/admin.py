from django.contrib import admin
from .models import Entry

# Register your models here.
from .models import Allcourses,details
admin.site.register(Allcourses)
admin.site.register(details)
admin.site.register(Entry)