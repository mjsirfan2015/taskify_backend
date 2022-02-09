from django.contrib import admin
from .models import *
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','name']

class TagAdmin(admin.ModelAdmin):
    list_display=['id','name']


class TaskAdmin(admin.ModelAdmin):
    list_display=['id','title','user','project','done']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Task,TaskAdmin)
