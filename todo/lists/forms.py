from django import forms
from .models import Tag,List,Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','notes','list','completed','priority','tags']

class ListForm(forms.ModelForm):
    class Meta:
        model=List
        fields=['name']
    
class TagForm(forms.ModelForm):
    class Meta:
        model=Tag
        fields=['name']