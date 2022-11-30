from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect
from  django.contrib import messages
from .forms import TravailForm, Structureform, PartenaireForm, TypeForm
from  gestioncontrat.models import Travail, Structure, Partenaire, Type

######################################################################################

#Zone to manage Type contrat

#############################################
# function to view Type contrat  
############################################

def type(request):
    types = Type.objects.all()
    context={"types":types}
    return render(request, 'gestioncontrat/type.html', context)


#############################################
# function to Create Type contrat  
############################################

def add_type(request):
    if request.method=="POST":
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully type contract was added !")
            return redirect('type')
        else:
            return render(request, 'gestioncontrat/add_type.html', {"form":form})
    else:
        form = TypeForm()
        return render(request, 'gestioncontrat/add_type.html', {"form":form})
    
    
#############################################
# function to edit Type contrat  
############################################ 
def edit_type(request, id):
    type = Type.objects.get(id=id)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save(id)
            messages.success(request, "successfully type contract was edited !")
            return redirect('type')
    else:
        form = TypeForm(instance=type)
    return render(request, 'gestioncontrat/edit_type.html', {'form':form})


#############################################
# function to delete Type contrat  
############################################ 

def delete_type(request, id):
    type = Type.objects.get(id = id)
    type.delete()
    messages.success(request, 'Type deleted successfully !')
    return HttpResponseRedirect("type")



######################################################################################

#Zone to manage structure

#############################################
# function to view Structure  
############################################

def structure(request):
    structures = Structure.objects.all()
    context={"structures":structures}
    return render(request, 'gestioncontrat/structure.html', context)


#############################################
# function to Create Structure  
############################################

def add_struct(request):
    if request.method=="POST":
        form = Structureform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Structure added successfully !")
            return redirect('structure')
        else:
            return render(request, 'gestioncontrat/add_struct.html', {"form":form})
    else:
        form = Structureform()
        return render(request, 'gestioncontrat/add_struct.html', {"form":form})
    
    
#############################################
# function to edit Structure  
############################################ 
def edit_struct(request, id):
    structure = Structure.objects.get(id=id)
    if request.method == 'POST':
        form = Structureform(request.POST, instance=structure)
        if form.is_valid():
            form.save(id)
            messages.success(request, "successfully type structure was edited !")
            return redirect('structure')
    else:
        form = Structureform(instance=structure)
    return render(request, 'gestioncontrat/edit_struct.html', {'form':form})


#############################################
# function to delete Structure  
############################################ 


def delete_struct(request, id):
    structure = Structure.objects.get(id = id)
    contrat.delete()
    messages.success(request, 'Structure deleted successfully !')
    return HttpResponseRedirect("structure")


#############################################################################

# Zone to manage Patenaire



############################################
# function to view Partenaire  
############################################

def partenaire(request):
    partenaires = Partenaire.objects.all()
    context={"partenaires":partenaires}
    return render(request, 'gestioncontrat/partenaire.html', context)


#############################################
# function to Create Partenaire  
############################################

def add_part(request):
    if request.method=="POST":
        form = PartenaireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Partenaire added successfully !")
            return redirect('partenaire')
        else:
            return render(request, 'gestioncontrat/add_part.html', {"form":form})
    else:
        form = PartenaireForm()
        return render(request, 'gestioncontrat/add_part.html', {"form":form})
    
    
#############################################
# function to edit Partenaire  
############################################ 
def edit_part(request, id):
    partenaire = Partenaire.objects.get(id=id)
    if request.method == 'POST':
        form = PartenaireForm(request.POST, instance=partenaire)
        if form.is_valid():
            form.save(id)
            messages.success(request, "successfully type partenaire was edited !")
            return redirect('partenaire')
    else:
        form = PartenaireForm(instance=partenaire)
    return render(request, 'gestioncontrat/edit_part.html', {'form':form})


#############################################
# function to delete Partenaire  
############################################ 

def delete_part(request, id):
    partenaire = Partenaire.objects.get(id = id)
    partenaire.delete()
    messages.success(request, 'Partenaire deleted successfully !')
    return HttpResponseRedirect("partenaire")


######################################################################################

#Zone to manage Contrat

#############################################
# function to view Contrat  
############################################

def contrat(request):
    contrats = Travail.objects.all()
    # paginator = Paginator(contrats, 4)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {"contrats":contrats}
    return render(request, 'gestioncontrat/contrat.html', context)

#############################################
# function to Create Contrat  
############################################

def add_contrat(request):
    if request.method=="POST":
        form = TravailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Contrat added successfully !")
            return HttpResponseRedirect('contrat')
        else:
            return render(request, 'gestioncontrat/add.html', {"form":form})
    else:
        form = TravailForm()
        return render(request, 'gestioncontrat/add.html', {"form":form})
       
       
#############################################
# function to edit Contrat  
############################################

def edit_contrat(request, id):
    contrat = Travail.objects.get(id=id)
    if request.method == 'POST':
        form = TravailForm(request.POST,request.FILES, instance=contrat)
        if form.is_valid():
            form.save(id)
            messages.success(request, "successfully!! contract was edited !")
            return redirect('contrat')
    else:
        form = TravailForm(instance=contrat)
    return render(request, 'gestioncontrat/edit.html', {'form':form})


#############################################
# function to delete Contrat  
############################################


def delete_contrat(request, id):
    contrat = Travail.objects.get(id=id)
    contrat.delete()
    messages.success(request, 'Contrat deleted successfully !')
    return HttpResponseRedirect("contrat")


# Create your views here.
