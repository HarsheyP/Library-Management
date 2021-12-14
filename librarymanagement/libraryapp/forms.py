from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from . import models

class LibrarianRegForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']

class StudentRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password']