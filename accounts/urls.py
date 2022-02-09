from django.urls import path

from accounts.views import *

urlpatterns = [
    path('',RegisterAPIView.as_view()),
    path('login',LoginView.as_view()),
    path('ping',Ping.as_view())
]
