from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth

# Create your views here.
def fun(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        data.save()
        return HttpResponse("Submitted")
    else:
        return render(request,'registration.html')
from django.contrib.auth.models import User

def user(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'view.html', {'users': users})
    
def log(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None and not user.is_superuser:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'invalid username or password'})
    else:
        return render(request,'login.html')
def index(request):
    return render(request,'index.html')
def home(request):
    a=User.objects.get(id=request.user.id)
    return render(request,'userhome.html',{'data':a})
def logout(request):
    auth.logout(request)
    return redirect('log')
def mainpage(request):
    return render(request,'mainpage.html')