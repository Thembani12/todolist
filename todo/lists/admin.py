from django.contrib import admin
from .models import Task,List,Tag

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['name','notes','list','completed','priority']
    prepopulated_fields={'slug':('name',)}

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}