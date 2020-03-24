from django.urls import path
from .views import Index, Contact, center
urlpatterns = [
    path('',Index.as_view(),name='Home'),
    path('contact/',Contact.as_view(),name='contact'),
    path('center/',center.as_view(),name='Exam_Centre')
]