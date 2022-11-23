from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect
from  django.contrib import messages
from .forms import ConventionForm
from  gestionconvention.models import Convention


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
# Create your views here.
