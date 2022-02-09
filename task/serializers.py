from dataclasses import field
from rest_framework import serializers

from task.models import *

class ProjectSer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Project

class TagSer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Tag

class TaskSer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Task