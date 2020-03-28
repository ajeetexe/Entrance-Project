from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from . import forms
from . import models
from django.shortcuts import get_object_or_404
from django.http import request


class Index(TemplateView):
    template_name = 'index.html'


class Contact(TemplateView):
    template_name = 'contact.html'


class center(TemplateView):
    template_name = 'center.html'

class register(CreateView):
    form_class = forms.RegisterForm
    model = User

class LoginPage(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'login_page.html'


class UserInfo(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    form_class = forms.UserInfoForm
    model = models.UserInfoModel

class Qualification(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    form_class = forms.QualifyForm
    model = models.QualificationModel

class DocumentUpload(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    form_class = forms.DocumentUploadForm
    model = models.DocumentUploadModel

class Preference(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    form_class = forms.PreferenceForm
    model = models.PreferenceModel

print(User.objects.filter())