from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('graph/<str:kind>/<str:time>', views.graph, name='graph'),
    path('board/list', views.board_list, name='board_list'),
    path('board/<int:board_id>', views.post, name='board')
    ]