from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserInfoModel, DocumentUploadModel, QualificationModel, PreferenceModel
from django.http import request


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2", ]

        widgets = {
            'password1': forms.PasswordInput(attrs={'class': "form-control"}),
            'password2': forms.PasswordInput(attrs={'class': "form-control"}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),

        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfoModel
        fields = ['userName', 'firstName', 'lastName', 'email',
                  'mobile', 'gender', 'dob', 'fullAddress', ]
        widgets = {
            'userName': forms.TextInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.DateInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'fullAddress': forms.Textarea(attrs={'class': 'form-control'}),
        }


class QualifyForm(forms.ModelForm):
    class Meta:
        model = QualificationModel
        fields = ['userName','degree1', 'percentage1', 'passYear1', 'university1', 'board1', 'degree2', 'percentage2',
                  'passYear2', 'university2', 'board2', 'degree3', 'percentage3', 'passYear3', 'university3', 'board3', ]
        widgets = {
            'UserName': forms.Select(attrs={'class': 'form-control'}),
            'degree1': forms.Select(attrs={'class': 'form-control'}),
            'percentage1': forms.TextInput(attrs={'class': 'form-control'}),
            'passYear1': forms.TextInput(attrs={'class': 'form-control'}),
            'university1': forms.TextInput(attrs={'class': 'form-control'}),
            'board1': forms.TextInput(attrs={'class': 'form-control'}),
            'degree2': forms.Select(attrs={'class': 'form-control'}),
            'percentage2': forms.TextInput(attrs={'class': 'form-control'}),
            'passYear2': forms.TextInput(attrs={'class': 'form-control'}),
            'university2': forms.TextInput(attrs={'class': 'form-control'}),
            'board2': forms.TextInput(attrs={'class': 'form-control'}),
            'degree3': forms.Select(attrs={'class': 'form-control'}),
            'percentage3': forms.TextInput(attrs={'class': 'form-control'}),
            'passYear3': forms.TextInput(attrs={'class': 'form-control'}),
            'university3': forms.TextInput(attrs={'class': 'form-control'}),
            'board3': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUploadModel
        fields = ['userName','pic1', 'pic2', 'pic3', 'pic4', ]
        widgets = {
            'UserName': forms.Select(attrs={'class': 'form-control'}),
            'pic1': forms.FileInput(attrs={'class': 'form-control'}),
            'pic2': forms.FileInput(attrs={'class': 'form-control'}),
            'pic3': forms.FileInput(attrs={'class': 'form-control'}),
            'pic4': forms.FileInput(attrs={'class': 'form-control'}),
        }


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = PreferenceModel
        fields = ['userName','course1', 'college1', 'course2',
                  'college2', 'course3', 'college3', ]
        widgets = {
            'UserName': forms.Select(attrs={'class': 'form-control'}),
            'course1': forms.Select(attrs={'class': 'form-control'}),
            'college1': forms.Select(attrs={'class': 'form-control'}),
            'course2': forms.Select(attrs={'class': 'form-control'}),
            'college2': forms.Select(attrs={'class': 'form-control'}),
            'course3': forms.Select(attrs={'class': 'form-control'}),
            'college3': forms.Select(attrs={'class': 'form-control'}),
        }

