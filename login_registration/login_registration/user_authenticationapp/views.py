from django.shortcuts import render,redirect
from .form import CustomUserForm,LoginForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout 

def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=CustomUserForm()
    return render(request,"register.html",{"form":form})

def loginpage(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)

            if user:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})

def logoutpage(request):
    logout(request)
    return redirect('login')

# Create your views here.
