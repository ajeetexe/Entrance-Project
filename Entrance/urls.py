from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index.as_view(),name='Home'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('center/',views.center.as_view(),name='Exam_Centre'),
    path('Register/',views.register.as_view(success_url="/"),name='register'),
    path('accounts/profile/',views.LoginPage.as_view(), name= 'user_profile'),
    path('userinfo/',views.UserInfo.as_view(),name='userinfo'),
    path('qualify/',views.Qualification.as_view(),name='qualify'),
    path('documentupload/',views.DocumentUpload.as_view(),name='documentupload'),
    path('preference/',views.Preference.as_view(),name='preference'),
]