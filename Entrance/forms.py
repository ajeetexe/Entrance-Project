from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.http import request


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2", ]

class FormFillForms(forms.ModelForm):
    class  Meta:
        model = FormFillModel
        fields = '__all__'
        


