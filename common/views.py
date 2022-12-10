from django.shortcuts import render

def security(request):
    return render(request, 'security.html')