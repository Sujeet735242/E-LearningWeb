# your_app_name/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/',HomePage, name='HomePage'),
    path('signup/',signUp, name='signUp'),
    path('login/',login,name='login'),
    path('loggedin/',handleLogin,name='handleLogin'),
    path('newuser/',handleSignUp, name='handleSignUp'),
    path('logout/',logout,name='logout'),
    path('learn/',courses,name='courses'),
]
