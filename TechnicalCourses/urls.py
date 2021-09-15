
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from . import views
app_name = 'TechnicalCourses'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('Name.html/', views.contact_form, name="inputform"),
    path('register.html/', views.login_acc, name='register'),
    path('testlogin.html/', views.add_user, name='register'),
    path('<int:couse_id>/', views.detail, name='detail'),
    path('<int:couse_id>/yourchoice', views.yourchoice, name='yourchoice'),
    path('', views.Courses, name='home-page'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    path('tag_detail.html/',  views.tag_detail, name='tag_detail_url'),
    path('tag.html/', views.tags_list, name='tags_list_url'),
    path('posts.html/', views.posts_list, name='posts_list_url'),
    path('accounts/login/', auth_views.LoginView.as_view()),



]
