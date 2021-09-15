
from django.db import models
import datetime
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
def __str__(self):
 return '{}'.format(self.title)


 class UserManager(BaseUserManager):
     def create_user(self,  email, password=None, is_staff=False, is_admin=False):
         if not password:
             raise ValueError("User must have a password")
         username_obj=self.model(self.normalize_email(email))
         username_obj.set_password(password)
         username_obj.save(using=self._db)
         return username_obj
         def create_staff(self,email, password=None):
             username=self.create_user(email, password=password, is_staff=True)
             return  username

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perm(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin

class Login(models.Model):
    new_user = models.TextField()
    password = models.CharField(max_length=10)
    password2 =models.CharField(max_length=10)
    def __str__(self):
        return 'register #{}'.format(self.id)


# Create your models here.
class Allcourses(models.Model):
    coursename=models.CharField(max_length=200)
    insname = models.CharField(max_length=100)
    startedfrom = models.DateTimeField('Started from')
    def __str__(self):
     return self.coursename

    def was_published_recently (self):
        return self.startedfrom >= timezone.now()- datetime.timedelta(days=1)

class details(models.Model):
    course=models.ForeignKey(Allcourses,on_delete=models.CASCADE)
    ct=models.CharField(max_length=500)
    your_choice=models.BooleanField(default=False)
    #sp=models.CharField(max_length=500)
    #il=models.CharField(max_length=500)
    def __str__(self):
       return str(self.pk)

