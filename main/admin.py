from django.contrib import admin
from rangefilter.filters import DateRangeFilter

# Register your models here.
from .models import Calender, User, Convenient, Fee, SecurityTodo, Board, CommunityPost, Comment, Visitor, \
    Notification


class FeeFilter(admin.ModelAdmin):
    search_fields = ['user__username']
    list_display = ('user', 'kind', 'fee', 'date_year', 'date_month')
    list_filter = ('kind', 'date_year', 'date_month')


class PostFilter(admin.ModelAdmin):
    search_fields = ('auther', 'title', 'contents')
    list_display = ('auther', 'title', 'date', 'board')
    list_filter = (('date', DateRangeFilter), 'board')


class NotiFilter(admin.ModelAdmin):
    search_fields = ('user', 'title', 'contents')
    list_display = ('user', 'title', 'date')
    list_filter = [('date', DateRangeFilter)]


class VisitorFilter(admin.ModelAdmin):
    search_fields = ['user__username', 'car']
    list_filter = [('date', DateRangeFilter)]
    list_display = ('user', 'date', 'car')

class CalenderFilter(admin.ModelAdmin):
    search_fields = ('content',)
    list_display = ('date', 'content')
    list_filter = [('date', DateRangeFilter)]

class TodoFilter(admin.ModelAdmin):
    search_fields = ('title', 'contents')
    list_display = ('title', 'date', 'deadline', 'status')
    list_filter = [('deadline', DateRangeFilter), 'status']


admin.site.register(User)
admin.site.register(Fee, FeeFilter)
admin.site.register(CommunityPost, PostFilter)
admin.site.register(Comment, PostFilter)
admin.site.register(Notification, NotiFilter)
admin.site.register(Visitor, VisitorFilter)
admin.site.register(Board)
admin.site.register(SecurityTodo)
admin.site.register(Convenient)
admin.site.register(Calender, CalenderFilter)
