from django.urls import path
from .views import RegisterClass
urlpatterns = [
    path('Register/',RegisterClass.as_view(),name='register'),
]