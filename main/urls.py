from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('graph/<str:state>', views.graph, name='graph'),
    ]