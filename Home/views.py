from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomePage(request):
    res=render(request,'landing_page.html')
    return HttpResponse(res)

def About(request):
    s='<h1>We are Devloper<h1>'
    return HttpResponse(s)