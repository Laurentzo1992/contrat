from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect
from  django.contrib import messages
from .forms import ConventionForm, TypeConventionForm
from  gestionconvention.models import Convention, TypeConvention


def convention(request):
    conventions = Convention.objects.all()
    context = {"conventions":conventions}
    return render(request, 'gestionconvention/convention.html', context)


def convention_add(request):
    if request.method=="POST":
        form = ConventionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Convention added successfully !")
            return redirect('convention')
        else:
            return render(request, 'gestionconvention/add.html', {"form":form})
    else:
        form = ConventionForm()
        return render(request, 'gestionconvention/add.html', {"form":form})


def convention_edit(request, id):
    convention = Convention.objects.get(id=id)
    if request.method == 'POST':
        form = ConventionForm(request.POST,request.FILES, instance=convention)
        if form.is_valid():
            form.save(id)
            messages.success(request, "successfully!! convention was edited !")
            return redirect('convention')
    else:
        form = ConventionForm(instance=convention)
    return render(request, 'gestionconvention/edit.html', {'form':form})


def convention_delete(request, id):
    convention = Convention.objects.get(id = id)
    convention.delete()
    messages.success(request, 'Convention deleted successfully !')
    return HttpResponseRedirect("convention")



def type_con(request):
    types_convs = TypeConvention.objects.all()
    context={"types_convs":types_convs}
    return render(request, 'gestionconvention/type_con.html', context)


def add_type_con(request):
    if request.method=="POST":
        form = TypeConventionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully type convention was added !")
            return redirect('type_con')
        else:
            return render(request, 'gestionconvention/add_type_conv.html', {"form":form})
    else:
        form = TypeConventionForm()
        return render(request, 'gestionconvention/add_type_conv.html', {"form":form})
    
    
#############################################
# function to edit Type contrat  
############################################ 
def edit_type_con(request, id):
    type_conv = TypeConvention.objects.get(id=id)
    if request.method == 'POST':
        form = TypeConventionForm(request.POST, instance=type_conv)
        if form.is_valid():
            form.save(id)
            messages.success(request, "successfully type Convention was edited !")
            return redirect('type_con')
    else:
        form = TypeConventionForm(instance=type_conv)
    return render(request, 'gestionconvention/edit_type_con.html', {'form':form})


#############################################
# function to delete Type contrat  
############################################ 

def delete_type_con(request, id):
    type_conv = TypeConvention.objects.get(id = id)
    type_conv.delete()
    messages.success(request, 'Type Convention deleted successfully !')
    return HttpResponseRedirect("type_con")


# Create your views here.
