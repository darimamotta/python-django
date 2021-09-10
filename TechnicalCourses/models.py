from django.db import models
import datetime
from django.utils import timezone
from django.shortcuts import reverse

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

def __str__(self):
        return '{}'.format(self.title)

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs={'slug':self.slug})
    def __str__(self):
        return '{}'.format(self.title)

class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)
    class Meta:
        verbose_name_plural = 'entries'

# Create your models here.
class Allcourses(models.Model):
    coursename=models.CharField(max_length=200)
    insname=models.CharField(max_length=100)
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