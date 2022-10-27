from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect
from  django.contrib import messages
from .forms import TravailForm
from  gestioncontrat.models import Travail, Categorie, Financement, Structure, Partenaire



def contrat(request):
    contrats = Travail.objects.all()
    # paginator = Paginator(contrats, 4)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {"contrats":contrats}
    return render(request, 'gestioncontrat/contrat.html', context)


def add_contrat(request):
    if request.method=="POST":
        form = TravailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Contrat added successfully !")
            return HttpResponseRedirect("contrat")
        else:
            return render(request, 'gestioncontrat/add.html', {"form":form})
    else:
        form = TravailForm()
        return render(request, 'gestioncontrat/add.html', {"form":form})
       
def edit_contrat(request, id):
    contrat = Travail.objects.get(id=id)
    if request.method == 'POST':
        form = TravailForm(request.POST,request.FILES, instance=contrat)
        if form.is_valid():
            form.save(id)
            return redirect('contrat')
    else:
        form = TravailForm(instance=contrat)
    return render(request, 'gestioncontrat/edit.html', {'form':form})



def delete_contrat(request, id):
    contrat = Travail.objects.get(id = id)
    contrat.delete()
    messages.success(request, 'Contrat deleted successfully !')
    return HttpResponseRedirect("contrat")
# Create your views here.
