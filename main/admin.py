from django.contrib import admin

# Register your models here.
from .models import park, Car, Fee, CCTV, SecurityTodo, Post, User, Notification, CommunityPost


class FeeSearch(admin.ModelAdmin):
    search_fields = ['kind']

admin.site.register(User)
admin.site.register(Fee, FeeSearch)
admin.site.register(CommunityPost)