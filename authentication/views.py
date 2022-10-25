from multiprocessing import context
from django.shortcuts import render, redirect
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import  login, logout, authenticate, get_user_model
from  django.contrib import messages
from authentication.models import User
User = get_user_model()
from django.contrib.auth.decorators import login_required #Login required
from  django.views.decorators.cache import cache_control # Destroy the section 


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    if request.user == None or request.user =="" or request.user.username == "":
        return render(request, "authentication/login.html")
    else:
        return HttpResponseRedirect('/')
    
# Login User
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('home')
        else:
            messages.error(request, "Please try again and enter corretly you username and you password")
            return HttpResponseRedirect('/')

# Deconnxion
def Logout_user(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')


# Page d'acceuil 

def home(request):
    return render(request, 'authentication/home.html')



#Function to create users

def add(request):
     if request.method=="POST":
        if request.POST.get('username') \
            and request.POST.get('password') \
            and request.POST.get('first_name') \
            and request.POST.get('last_name') \
            and request.POST.get('email'):
            user_user = User()
            user_user.username = request.POST.get('username')
            user_user.password = request.POST.get('password')
            user_user.first_name = request.POST.get('first_name')
            user_user.last_name = request.POST.get('last_name')
            user_user.email = request.POST.get('email')
            user_user.save()
            messages.success(request, "User added successfully !")
            return HttpResponseRedirect("list_user") 
        else: 
            return render(request, 'authentication/create.html')
# Edit user create function
#@login_required
def edit(request):
    if request.method == "POST":
        user_user = User.objects.get(id = request.POST.get('id'))
        if user_user != None:
            user_user.username = request.POST.get('username')
            user_user.password = request.POST.get('password')
            user_user.first_name = request.POST.get('first_name')
            user_user.last_name = request.POST.get('last_name')
            user_user.email = request.POST.get('email')
            user_user.save()
            messages.success(request, "User updated successfully !")
            return HttpResponseRedirect("users")
#---------------------------------------------------------------------------
# Edit user create function

#@login_required
def delete(request,user_id):
    citoyen = User.objects.get(id = user_id)
    citoyen.delete()
    messages.success(request, 'User deleted successfully !')
    return HttpResponseRedirect("users")
    
# List user  function
def users(request):
    user_lists = User.objects.all()
    return render(request, "authentication/list.html", {"user_lists":user_lists})


def profile(request):
    context = {}
    return render(request, "authentication/profile.html", context)



def statistique(request):
    context = {}
    return render(request, "authentication/statistique.html", context)

# Create your views here.
