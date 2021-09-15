from django import forms
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]




class TagForm(forms.Form):
        title = forms.CharField(max_length=50)
        slug = forms.CharField(max_length=50)




class LoginForm(forms.Form):
        username = forms.CharField(label='Your name', max_length=100)
        password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)




class Contact(forms.Form):
            subject = forms.CharField(max_length=100)
            message = forms.CharField(widget=forms.Textarea)
            sender = forms.EmailField()
            cc_myself = forms.BooleanField(required=False)

class Register(forms.ModelForm):
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


