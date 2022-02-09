from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)

class Tag(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)

class Task(models.Model):
    PRIORITY=(
        ('high','High'),
        ('medium','Medium'),
        ('low','Low')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    title=models.CharField(max_length=140)
    description=models.CharField(max_length=500)
    priority=models.CharField(choices=PRIORITY,max_length=6)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    done=models.BooleanField(default=False)

    