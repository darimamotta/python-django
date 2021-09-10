from django import forms
from django.forms import ModelForm
from .models import Entry

class TagForm(forms.Form):
        title = forms.CharField(max_length=50)
        slug = forms.CharField(max_length=50)

class RegisterForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)

class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)


