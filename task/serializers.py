from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from task.models import *

class ProjectSer(serializers.ModelSerializer):
    user = user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),queryset=User.objects.all())
    class Meta:
        fields='__all__'
        model=Project

class TagSer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Tag

class TaskSer(serializers.ModelSerializer):
    status= serializers.CharField(source='tag.name')
    class Meta:
        fields='__all__'
        model=Task