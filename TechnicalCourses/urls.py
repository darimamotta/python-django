from django.urls import path
from .import views
app_name = 'TechnicalCourses'
urlpatterns = [
    path('Name.html/', views.get_name, name="inputform"),
    path('register.html/', views.register_acc, name='registration'),
    path('<int:couse_id>/', views.detail, name='detail'),
    path('<int:couse_id>/yourchoice', views.yourchoice, name='yourchoice'),
    path('', views.Courses, name='home-page')
]
