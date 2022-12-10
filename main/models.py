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
class Convenient(models.Model):
    title = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    content = models.TextField()
    cost = models.CharField(max_length=50)

class Fee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kind = models.CharField(max_length=50)
    fee = models.IntegerField()
    date_year = models.IntegerField()
    date_month = models.IntegerField()

    type_dict = {"electric": "전기", "water": "수도", "gas": "가스", "waste": "음식물"}

    def __str__(self):
        return f"{self.type_dict[self.kind]}요금 {self.user.username}님 {self.date_year}년 {self.date_month}월"
#security
class CCTV(models.Model):
    address = models.CharField(max_length=100)
    floor = models.IntegerField()

class security_todo(models.Model):
    date = models.DateTimeField()
    deadline = models.DateTimeField()
    title = models.CharField(max_length = 20)
    contents = models.TextField()
    status = models.IntegerField()

#commuity

class Post(models.Model):
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    contents = models.TextField()

class CommunityPost(Post):
    isAnonymous = models.BooleanField()
    board = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.board}|{self.title}"

class Comment(Post):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE)

class complaints(Post):
    category = models.CharField(max_length=20)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    read = models.BooleanField()
    date = models.DateTimeField()
    title = models.CharField(max_length=20)
    contents = models.TextField()

#complaints