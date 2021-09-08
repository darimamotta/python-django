from django import forms
from django.forms import ModelForm
from .models import Entry



class RegisterForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)

class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)
