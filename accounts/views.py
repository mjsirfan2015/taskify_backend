from django.conf import settings
from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from accounts.serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterAPIView(generics.CreateAPIView):
    permission_classes=[AllowAny,]
    serializer_class=RegisterSerializer

class LoginView(generics.GenericAPIView,mixins.CreateModelMixin):
    permission_classes=[AllowAny]
    serializer_class=LoginSerializer
    
    def post(self,request):
        response = self.create(request)
        if response.status_code!=201:return response
        refresh=RefreshToken.for_user(User.objects.get(email=response.data.get("email",None)))# get jwt tokens
        tokens={
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        response.set_cookie(
                key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                value = tokens["access"],
                expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                httponly = True,
            )
        return response

class Ping(APIView):
    def get(self,request):
        return Response("hi ping")