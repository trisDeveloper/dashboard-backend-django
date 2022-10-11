from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser


class Dashuser (models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    userimage = models.ImageField(upload_to='userimages/', blank=True, null=True)
    country = models.CharField(max_length=250, blank=True)
    birthday = models.DateField(blank=True)
    joindate = models.DateField(blank=True)
    city = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return self.username
    
class Todolist (models.Model):
    userid = models.IntegerField()
    todoid = models.AutoField(primary_key=True)
    name = models.TextField()
    newname = models.TextField(blank=True)
    start = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=250, blank=True)
    done = models.BooleanField()
    dialog = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class Linkslist (models.Model):
    userid = models.IntegerField()
    linkid = models.AutoField(primary_key=True)
    name = models.TextField()
    urlpath = models.CharField(max_length=50, blank=True)
    dialog = models.BooleanField()
    
    def __str__(self):
        return self.name
    
