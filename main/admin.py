from django.contrib import admin

# Register your models here.
from .models import park, Car, Amenities, Fee, CCTV, security_todo, Comment, Post, board, User, Notification

admin.site.register(User)
admin.site.register(Fee)