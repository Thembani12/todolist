from django.urls import path
from . import views


urlpatterns=[
    #path('',views.list,name='list'),
    path('',views.task_list,name='task-list'),
    path('<slug:list_slug>/',views.task_list,name='task-by-lists'),
    path('<int:id>/<slug:slug>/',views.detail,name='task-detail'),
] 