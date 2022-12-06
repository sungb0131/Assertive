from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('graph/<str:kind>/<str:time>', views.graph, name='graph')
    ]