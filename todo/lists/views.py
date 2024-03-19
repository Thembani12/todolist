from django.shortcuts import render,get_object_or_404,redirect
from .models import Task,List,Tag
from .forms import TaskForm,TagForm,ListForm


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

def create_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            task=form.save()
        return render(request,"lists/create_task.html",{'task':task})
    else:
        form=TaskForm()
    return render(request,"lists/todos/task_form.html",{'form':form,'task':task})

def create_list(request):
    if request.method=='POST':
        form=ListForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            list=form.save()
        return render(request,"lists/create_list.html",{'list':list})
    else:
        form=ListForm()
    return render(request,"lists/todos/list_form.html",{'form':form,'list':list})

def create_tag(request):
    if request.method=='POST':
        form=TagForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            tag=form.save()
        return render(request,"lists/create_tag.html",{'tag':tag})
    else:
        form=TagForm()
    return render(request,"lists/todos/tag_form.html",{'form':form,'tag':tag})