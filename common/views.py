from django.shortcuts import render
from main.models import SecurityTodo

def security(request):
    return render(request, 'security.html', {
        'todos': SecurityTodo.objects.all().order_by('-date')
    })