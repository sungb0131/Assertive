from django.contrib import admin

# Register your models here.
from .models import Calender, User, Parking, Convenient, Fee, SecurityTodo, Board, Post


class FeeFilter(admin.ModelAdmin):
    list_display = ('user', 'kind', 'fee', 'date_year', 'date_month')
    list_filter = ('user', 'kind', 'date_year', 'date_month')

class PostFilter(admin.ModelAdmin):
    list_display = ('auther', 'title', 'date', 'board')
    list_filter = ('auther', 'title', 'date', 'board')

    @admin.display(description='게시판', ordering='board__name')
    def get_board(self, obj):
        return obj.board.name

admin.site.register(User)
admin.site.register(Fee, FeeFilter)
admin.site.register(Post, PostFilter)
admin.site.register(Board)
admin.site.register(SecurityTodo)
admin.site.register(Convenient)
admin.site.register(Parking)
admin.site.register(Calender)