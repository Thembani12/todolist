from django.urls import path
from . import views


urlpatterns=[
    #path('',views.list,name='list'),
    path('',views.task_list,name='task-list'),
    path('<slug:list_slug>/',views.task_list,name='task-by-lists'),
    path('<int:id>/<slug:slug>/',views.detail,name='task-detail'),
    path('create-task/',views.create_task,name='create-task'),
    path('create-list/',views.create_list,name='create-list'),
    path('create-tag',views.create_tag,name='create-tag'),
] 