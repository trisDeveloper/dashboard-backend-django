from django.shortcuts import render
from .models import Dashuser, Todolist, Linkslist
from .serializers import DashSerializer, TodoSerializer , LinkSerializer 
from rest_framework import viewsets

class UserListApiView(viewsets.ModelViewSet):

    queryset = Dashuser.objects.all() 
    serializer_class = DashSerializer 

class TodoListApiView(viewsets.ModelViewSet):
    
    queryset = Todolist.objects.all() 
    serializer_class = TodoSerializer 
class LinkListApiView(viewsets.ModelViewSet):
    
    queryset = Linkslist.objects.all() 
    serializer_class = LinkSerializer 