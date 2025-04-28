from django.urls import path,include
from  django.contrib import admin
from basic_app import views

#template tagging
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'), #name='register' is what connects the URL to {% url 'register' %} inside templates.
    path('user_login/', views.user_login, name='user_login'), #name='user_login' is what connects the URL to {% url 'user_login' %} inside templates
    

    ]
 

 