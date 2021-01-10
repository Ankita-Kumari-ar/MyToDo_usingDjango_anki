from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Todo
class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=64, required=False, help_text='Optional')
    last_name=forms.CharField(max_length=64, required=False, help_text='Optional')
    email=forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2',)

class NewForm(ModelForm):
    text=forms.CharField(max_length=254,label="")
    class Meta:
        model=Todo
        fields=['text']