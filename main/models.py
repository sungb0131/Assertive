from django.db import models
from config import settings
from django.contrib.auth.models import AbstractUser

#main date
class Calender(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=30)

class User(AbstractUser):
    car = models.CharField(max_length=8, null=True)
    phone = models.CharField(max_length=11)

#convenience0
class Convenient(models.Model):
    title = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    content = models.TextField()
    cost = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

class Fee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kind = models.CharField(max_length=50)
    fee = models.IntegerField()
    date_year = models.IntegerField()
    date_month = models.IntegerField()

    type_dict = {"electric": "전기", "water": "수도", "gas": "가스", "waste": "음식물"}

    def __str__(self):
        return f"{self.type_dict[self.kind]}요금 {self.user.username}님 {self.date_year}년 {self.date_month}월"

class SecurityTodo(models.Model):
    date = models.DateTimeField()
    deadline = models.DateTimeField()
    title = models.CharField(max_length = 20)
    contents = models.TextField()
    status = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

#commuity
class Board(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    contents = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    isAnonymous = models.BooleanField()

class CommunityPost(Post):
    pass

    def __str__(self):
        return f"{self.board}|{self.title}"

class Comment(Post):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=20)
    contents = models.TextField()

class Parking(models.Model):
    floor = models.IntegerField()
    status = models.TextField()
    space = models.IntegerField()

class Visitor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    car = models.CharField(max_length=8)
