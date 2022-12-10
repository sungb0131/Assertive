from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('graph/<str:kind>/<str:time>', views.graph, name='graph'),
    path('board/list/<int:board_id>', views.board_list, name='board_list'),
    path('board/<int:post_id>', views.view_post, name='board'),
    path('conv/', views.conv, name='conv'),
    path('board/<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('board/write/<int:board_id>', views.write, name='write'),
    path('board/write/<int:board_id>/submit', views.write_post, name='write_post'),
    ]