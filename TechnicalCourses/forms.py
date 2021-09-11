from django import forms
from django.forms import ModelForm
from .models import Entry
from django.contrib.auth.models import User

class TagForm(forms.Form):
        title = forms.CharField(max_length=50)
        slug = forms.CharField(max_length=50)
class RegisterForm(forms.Form):
   your_name=forms.CharField(label='Your Name', max_length=100)
   password = forms.CharField(label='Your password', widget=forms.PasswordInput)



class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)
        password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

        from django import forms

class ContactForm(forms.Form):
            subject = forms.CharField(max_length=100)
            message = forms.CharField(widget=forms.Textarea)
            sender = forms.EmailField()
            cc_myself = forms.BooleanField(required=False)

class UserRegistrationForm(forms.ModelForm):
                password = forms.CharField(label='Password', widget=forms.PasswordInput)
                password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

class Meta:
                        model = User
                        fields = ('username', 'first_name', 'email')

def clean_password2(self):
                        cd = self.cleaned_data
                        if cd['password'] != cd['password2']:
                                raise forms.ValidationError('Passwords dont match.')
                        return cd['password2']


