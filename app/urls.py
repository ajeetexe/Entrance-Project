from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.urls import path
from django.views.generic import TemplateView, CreateView

from app import views
from app.forms import RegisterForms

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('centre/', TemplateView.as_view(template_name='center.html'), name='centre'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('register/', CreateView.as_view(model=User, form_class=RegisterForms, success_url='/login/'), name='register'),
    path('accounts/profile/', views.login_page, name='login-page'),
    path('form-fill/', views.FormFillView.as_view(), name='form-fill'),
    path('user-detail/<slug>/', views.UserDetailView.as_view(), name='user-detail'),
    path('hallticket/', views.pdf_generator, name='pdf-generator'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
