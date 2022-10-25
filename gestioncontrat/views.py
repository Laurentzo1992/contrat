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
    paginator = Paginator(contrats, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj}
    return render(request, 'gestioncontrat/contrat.html', context)


def add(request):
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
       
def edit(request):
    if request.method == "POST":
        contrat = Travail.objects.get(id = request.POST.get('id'))
        if contrat != None:
            contrat.reference = request.POST.get('reference')
            contrat.objet = request.POST.get('objet')
            contrat.nature = request.POST.get('nature')
            contrat.matricule = request.POST.get('matricule')
            contrat.nom = request.POST.get('nom')
            contrat.prenom = request.POST.get('prenom')
            contrat.montant = request.POST.get('montant')
            contrat.duree = request.POST.get('duree')
            contrat.date_signature = request.POST.get('date_signature')
            contrat.date_debut = request.POST.get('date_debut')
            contrat.date_fin = request.POST.get('date_fin')
            contrat.nombre_renouv = request.POST.get('nombre_renouv')
            contrat.date_renouvel = request.POST.get('date_renouvel')
            contrat.lieu = request.POST.get('lieu')
            contrat.date_alerte = request.POST.get('date_alerte')
            contrat.file = request.POST.get('file')
            contrat.save()
            messages.success(request, "Contrat updated successfully !")
            return HttpResponseRedirect("index")
        
def delete(request, id):
    contrat = Travail.objects.get(id = id)
    contrat.delete()
    messages.success(request, 'Contrat deleted successfully !')
    return HttpResponseRedirect("index")
# Create your views here.
