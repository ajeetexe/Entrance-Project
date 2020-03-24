from django.views.generic import TemplateView
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'



class Contact(TemplateView):
    template_name = 'contact.html'


class center(TemplateView):
    template_name = 'center.html'