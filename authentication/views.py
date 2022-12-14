from multiprocessing import context
from django.shortcuts import render, redirect
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import  login, logout, authenticate, get_user_model
from django.contrib.auth.models import Group, Permission
from  django.contrib import messages
from authentication.models import User
from gestioncontrat.models import Travail
from gestionconvention.models import Convention
from  . import forms
User = get_user_model()
from django.contrib.auth.decorators import login_required #Login required
from  django.views.decorators.cache import cache_control # Destroy the section
from django.db.models import  Count


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
    conts = Travail.objects.all()
    contrats = conts.count()
    cont_archs = Travail.objects.filter(archive=True).count()
    convents = Convention.objects.all()
    conventions = convents.count()
    users = User.objects.all()
    users = users.count()
    results = conts.values('type').annotate(dcount=Count('type')).order_by('dcount')
    results_conv = convents.values('type').annotate(c_count=Count('type')).order_by('c_count')
    context = {"contrats":contrats, "conventions":conventions, "conts":conts, "convents":convents, "results":results, "results_conv":results_conv, "users":users, "cont_archs":cont_archs}
    return render(request, 'authentication/home.html',context )



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

# User  profile function
def profile(request):
    user = User.objects.get(id=request.user.pk)
    context = {"user":user}
    if request.method == 'POST':
        form = forms.CreateUser(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save(id)
            return redirect('profile')
    else:
        form = forms.CreateUser(instance=user)
    return render(request, "authentication/profile.html", context)



def statistique(request):
    context = {}
    return render(request, "authentication/statistique.html", context)


#Function to create users
def add_user(request):
    form = forms.CreateUser()
    if request.method == 'POST':
        form = forms.CreateUser(request.POST,request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'authentication/add.html', context={'form':form})

# Edit user edit function
def edit_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CreateUser(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save(id)
            return redirect('list')
    else:
        form = forms.CreateUser(instance=user)
    return render(request, 'authentication/edit.html', {'form':form})



def delete_user(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('list')
    return render(request, 'authentication/delete.html', {'user':user})

#----------

# Create your views here.
