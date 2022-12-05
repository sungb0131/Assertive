from django.shortcuts import render
from django.http import HttpResponse

from .models import Fee
# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def graph(request):
    label = ["water", "electric", "gas", "administration", "food_waste"]
    for idx, i in enumerate(Fee.objects.all()):
        data = [f"{i.date/100}년{i.date%100}월", [i.water, i.electric, i.gas, i.administration, i.food_waste]]

    return render(request, 'graph.html', {'labels': label, 'data': data})