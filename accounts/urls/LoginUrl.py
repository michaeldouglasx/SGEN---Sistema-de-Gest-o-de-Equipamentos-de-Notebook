from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..views.LoginView import Login_View


urlpatterns = [
    path('login/', Login_View, name='login'),
    
] 
