from django import forms
from . import models 

class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.Register
        fields =['fullName','email','mobile','dob','gender','password']
        widget = {
            'password':forms.PasswordInput(attrs={'class':"form-control"}),
            'fullName':forms.TextInput(attrs={'class': 'form-control'}),   
            'mobile':forms.NumberInput(attrs={}),
            'dob':forms.DateField(),
            'email':forms.EmailInput(attrs={'class':"form-control",'placeholder':"Enter email"})
        }