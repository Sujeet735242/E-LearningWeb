# your_app_name/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('home-page/',HomePage, name='HomePage'),
    path('about/',About, name='About'),
]
