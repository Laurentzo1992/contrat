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
            conv_ref = form.cleaned_data.get('reference')
            messages.success(request, f"convention {conv_ref} added successfully !")
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
            messages.success(request, f"successfully!! {convention.reference} was edited !")
            return redirect('convention')
    else:
        form = ConventionForm(instance=convention)
    return render(request, 'gestionconvention/edit.html', {'form':form})


def convention_delete(request, id):
    convention = Convention.objects.get(id = id)
    if request.method=='POST':
        convention.delete()
        messages.success(request, f'{convention.reference} deleted successfully !')
        return redirect("convention")
    return render(request, 'gestionconvention/convention_delete.html', {"convention":convention})



def type_con(request):
    types_convs = TypeConvention.objects.all()
    context={"types_convs":types_convs}
    return render(request, 'gestionconvention/type_con.html', context)


def add_type_con(request):
    if request.method=="POST":
        form = TypeConventionForm(request.POST)
        if form.is_valid():
            form.save()
            type_conv = form.cleaned_data.get('libelle')
            messages.success(request, f"successfully {type_conv} was added !")
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
            messages.success(request, f"successfully {type_conv.libelle} was edited !")
            return redirect('type_con')
    else:
        form = TypeConventionForm(instance=type_conv)
    return render(request, 'gestionconvention/edit_type_con.html', {'form':form})


#############################################
# function to delete Type contrat  
############################################ 

def delete_type_con(request, id):
    type_conv = TypeConvention.objects.get(id = id)
    if request.method=='POST':
        type_conv.delete()
        messages.success(request, f'{type_conv.libelle} deleted successfully !')
        return redirect("type_con")
    return render(request, 'gestionconvention/delete_type_con.html', {"type_conv":type_conv})



# Create your views here.
