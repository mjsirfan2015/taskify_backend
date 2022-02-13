import uuid
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ErrorDetail

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','email','password']
    
    def create(self,instance):
        user=User.objects.create_user(email=instance['email'],password=instance['password'],
        first_name=instance['first_name'],last_name=instance['last_name'],username=uuid.uuid4().hex)
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password']
    
    def create(self,instance):
        user=User.objects.filter(email=instance.get("email"))
        if not user.exists():raise serializers.ValidationError({'login':
                ErrorDetail(code='invalid_login',string='Password or Email Incorrect')})
        user=authenticate(username=user[0].username\
            ,password=instance.get("password",None))
        if user is None:
            raise serializers.ValidationError({'login':
                ErrorDetail(code='invalid_login',string='Password or Email Incorrect')})
        return user