from rest_framework import generics

from task.serializers import *
# Create your views here.

class ProjectAPIView(generics.ListCreateAPIView,\
    generics.UpdateAPIView,generics.DestroyAPIView):
    '''
    CRUD for Project
    '''
    serializer_class=ProjectSer
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class TagAPIView(generics.ListCreateAPIView,\
    generics.UpdateAPIView,generics.DestroyAPIView):
    '''
    CRUD for Tags
    '''
    serializer_class=TagSer
    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

class TaskAPIView(generics.ListCreateAPIView,\
    generics.UpdateAPIView,generics.DestroyAPIView):
    '''
    CRUD for Task
    '''
    serializer_class=TagSer

    def put(self, request):
        return self.partial_update(request)
    
    def get_queryset(self):
        project = self.kwargs.get('project',None)
        if project is not None:
            return Task.objects.filter(project__id=project,user__in=[self.request.user,None])
        
        return Task.objects.all()
