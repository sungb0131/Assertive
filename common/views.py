from django.shortcuts import render, redirect
from main.models import SecurityTodo

def security(request):
    if not request.user.is_staff:
        return redirect('/')
    return render(request, 'security.html', {
        'todos': SecurityTodo.objects.all().order_by('date', 'status')
    })

def todo(request, todo_id, status):
    todo = SecurityTodo.objects.get(id=todo_id)
    todo.status = status
    todo.save()
    return redirect('/security')

def index(request):
    if str(request.user) != 'AnonymousUser':
        if request.user.is_superuser:
            return redirect('/admin')
        elif request.user.is_staff:
            return redirect('/security')
        else:
            return redirect('/main')
    else:
        return redirect('/login')
