from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from . import forms
from . import models
from django.shortcuts import get_object_or_404, redirect, render
from django.http import request
from django.contrib.auth.decorators import login_required

class Index(TemplateView):
    template_name = 'index.html'


class Contact(TemplateView):
    template_name = 'contact.html'


class center(TemplateView):
    template_name = 'center.html'

class register(CreateView):
    form_class = forms.RegisterForm
    model = User

class FormFillView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = forms.FormFillForms
    model = models.FormFillModel


@login_required
def loginPage(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return render(request,'login_page.html')