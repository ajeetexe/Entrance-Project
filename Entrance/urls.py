from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index.as_view(),name='Home'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('center/',views.center.as_view(),name='Exam_Centre'),
    path('Register/',views.register.as_view(success_url="/"),name='register'),
    path('accounts/profile/',views.loginPage, name= 'user_profile'),
    path('formfill/',views.FormFillView.as_view(),name='form_fill')
]