from django.shortcuts import render
from .models import Dashuser 
from .serializers import WorkSerializer 
from rest_framework import viewsets

class UserListApiView(viewsets.ModelViewSet):

    queryset = Dashuser.objects.all() 
    serializer_class = WorkSerializer 