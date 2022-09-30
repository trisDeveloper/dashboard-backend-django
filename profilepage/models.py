
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.core.files import File

#from django.contrib.auth.models import User
# Create your models here.
class Dashuser (models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    userimage = models.ImageField(upload_to='userimages/', blank=True)
    country = models.CharField(max_length=250, blank=True)
    birthday = models.DateField(blank=True)
    joindate = models.DateField(blank=True)
    events = []
    links = []
    city = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return self.username
    

