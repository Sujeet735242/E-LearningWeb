from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def HomePage(request):
    res=render(request,'landing_page.html')
    return HttpResponse(res)

def signUp(request):
    res=render(request,'sign_up.html')
    return HttpResponse(res)

def handleSignUp(request):
    if request.method=='POST':
        #Get the post parameters
        username=request.POST['username']
        password=request.POST['password']
        con_password=request.POST['con_password']

        #check for errorneous inputs
        

        #create the user
        myuser=User.objects.create_user(username,password)
        myuser.save()
        messages.success(request, "Your UpSkillNow account has been successfully created")
        return redirect('/Home/login/')
    else:
        return HttpResponse('404 - Not Found')

def login(request):
    res=render(request,'login.html')
    return HttpResponse(res)

def handleLogin(request):
    if request.method=='POST':
        #get the Login data by POST method
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            print("Login attempt with username:", loginusername)
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/Home/homepage/')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('/Home/login/')
def courses(request):
    res=render(request,'logged_in_page.html')
    return HttpResponse(res)

def logout(request):
    pass