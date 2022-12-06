from django.db import models
from config import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    car = models.CharField(max_length=8)
    phone = models.CharField(max_length=11)

class park(models.Model):
    date = models.DateTimeField()

class Car(models.Model):
    type = models.CharField(max_length=50)
    visitor = models.BooleanField()

#convenience0
class Amenities(models.Model):
    date = models.DateTimeField()
    memo = models.CharField(max_length = 100)

class Fee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kind = models.CharField(max_length=50)
    fee = models.IntegerField()
    date_year = models.IntegerField()
    date_month = models.IntegerField()

#security
class CCTV(models.Model):
    address = models.CharField(max_length=100)
    floor = models.IntegerField()

class security_todo(models.Model):
    date = models.DateTimeField()
    deadline = models.DateTimeField()
    title = models.CharField(max_length = 20)
    contents = models.TextField()
    status = models.FloatField()

#commuity
class Comment(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=20)
    isAnonymous = models.BooleanField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    contents = models.TextField()
    isAnonymous = models.BooleanField()

class board(models.Model):
    category = models.CharField(max_length=20)

class Notification(models.Model):
    read = models.BooleanField()
    date = models.DateTimeField()
    title = models.CharField(max_length=20)
    contents = models.TextField()

#complaints
class complaints(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    contents = models.TextField()