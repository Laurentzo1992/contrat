from multiprocessing import context
from django.shortcuts import render
from urllib import request, response
from django.http import HttpResponseRedirect

import gestionconvention


def convention(request):
    context = {}
    return render(request, 'gestionconvention/convention.html', context)
    
# Create your views here.
