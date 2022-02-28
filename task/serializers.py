from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from task.models import *

class ProjectSer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),queryset=[serializers.CurrentUserDefault()])
    class Meta:
        fields=['id','user','name']
        model=Project

class TagSer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),queryset=[serializers.CurrentUserDefault()])
    class Meta:
        fields=['id','user','name']
        model=Tag

class TaskSer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status= serializers.CharField(source='tag.name',read_only=True)
    class Meta:
        fields=['id','user','status','project','title','description','priority','tag','done','scheduled','date']
        model=Task