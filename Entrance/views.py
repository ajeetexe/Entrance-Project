from django.views.generic import TemplateView, CreateView
from . import forms
from . import models
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'



class Contact(TemplateView):
    template_name = 'contact.html'


class center(TemplateView):
    template_name = 'center.html'

class register(CreateView):
    form_class = forms.RegisterForm

    model = models.Register