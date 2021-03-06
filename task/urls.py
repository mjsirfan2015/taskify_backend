
from django.urls import path
from .views import *

urlpatterns = [
    path('project',ProjectAPIView.as_view()),
    path('tag',TagAPIView.as_view()),
    path('tag/<int:pk>',TaskAPIView.as_view()),
    path('',TaskAPIView.as_view()),
    path('<int:pk>',TaskAPIView.as_view()),
]
