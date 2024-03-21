from django.shortcuts import render
from product.models import product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")   

def home(request):
    username=request.session.get("currentUser",None)
    return render(request,"index.html",{"username":username}) 
    

@login_required(login_url="/login/")
def search(request):
    query=request.GET.get('query','')
    #print(query)
    products=product.pm.all().filter(product_name__icontains=query)
    return render(request,"search.html",{"allproducts":products})  


def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        #form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RegisterForm()    
        #form=UserCreationForm()
    return render(request,"register.html",{"form":form})

def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            
            #Authentication
            user=authenticate(username=username,password=password)
         
            if user is not None:
                login(request,user)
                request.session["currentUser"]=user.get_username()#if it is not found it goes to home page

                return HttpResponseRedirect("/")

    else:    
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})              



#user logout function

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")