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
    serializer_class=TaskSer
    lookup_field = 'pk'
    def put(self, request,pk):
        return self.partial_update(request,pk)
    
    def get_queryset(self):
        project = str(self.request.GET.get('project',''))
        if project is not None and project.isnumeric():
            return Task.objects.filter(project__id=int(project),user__in=[self.request.user,None],done=False)
        
        return Task.objects.filter(user=self.request.user,done=False)
