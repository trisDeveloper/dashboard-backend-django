from rest_framework import serializers
from .models import Dashuser

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashuser
        fields = ('id', 'username', 'email', 'password', 'userimage', 'country', 'birthday', 'joindate', 'events', 'links', 'city')