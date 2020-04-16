from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import FormFill


class RegisterForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class FormFillForm(forms.ModelForm):
    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].capitalize()

    class Meta:
        model = FormFill
        fields = '__all__'
        exclude = ['user_name', ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', }),
        }
