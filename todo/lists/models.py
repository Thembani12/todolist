from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

class List(models.Model):
    name=models.CharField(max_length=255,help_text='list name')
    slug=models.CharField(max_length=255,unique=True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('task-by-lists',args=[self.slug])
    
    
    
    
class Task(models.Model):
    PRIORITY= {
        "N":"None",
        "L":"Low",
        "M":"Medium",
        "H":"High",
    }
    name=models.CharField(max_length=255, help_text='task name')
    slug=models.CharField(max_length=100)
    notes=models.TextField(blank=True, help_text='add')
    list=models.ForeignKey(List,on_delete=models.CASCADE,related_name='tasks', default='my list')
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=False)
    priority=models.CharField(max_length=1,choices=PRIORITY, default='N')
    tags=models.ManyToManyField(Tag,blank=True, related_name='tags')

    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=["-created"]
    
    def get_absolute_url(self):
        return reverse('task-detail',args=[self.id, self.slug])