from django.shortcuts import render
from django.http import HttpResponse

from .models import Fee

def index(request):
    
    return render(request, 'index2.html', {'plans': [1,1,1,1,1,1,1]})

def graph(request, state):
    if state == 'both':
        return render(request, 'gass_index.html')
    elif state == 'now':
        return render(request, 'live_gass_index.html')
    elif state == 'prev':
        return render(request, 'pre_gass_index.html')