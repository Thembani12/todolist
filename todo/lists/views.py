from django.shortcuts import render,get_object_or_404
from .models import Task,List,Tag

# Create your views here.
def list(request,list_slug=None):
    tasks=Task.objects.all()
    lists=List.objects.all()
    list=None
    if list_slug:
        list=get_object_or_404(List,slug=list_slug)
        tasks=tasks.filter(list=list)
    return render(request,"lists/list.html",{'lists':lists,'tasks':tasks})


def task_list(request,list_slug=None):
    lists=List.objects.all()
    tasks=Task.objects.all()
    list=None
    if list_slug:
        list=get_object_or_404(List,slug=list_slug)
        tasks=tasks.filter(list=list)
    return render(request,"lists/index.html",
    {'tasks':tasks,'lists':lists,'list':list})
    

def detail(request,id,slug):
    task=get_object_or_404(Task,id=id,slug=slug)
    return render(request,"lists/detail.html",{'task':task})