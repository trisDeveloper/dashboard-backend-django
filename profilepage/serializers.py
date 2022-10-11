from rest_framework import serializers
from .models import Dashuser, Todolist, Linkslist

class DashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashuser
        fields = ('id', 'username', 'email', 'password', 'userimage', 'country', 'birthday', 'joindate', 'city')
        
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('userid', 'todoid', 'name', 'newname', 'start', 'color', 'done', 'dialog')
        
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linkslist
        fields = ('userid', 'linkid', 'name', 'urlpath', 'dialog')