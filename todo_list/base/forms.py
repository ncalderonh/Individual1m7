from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
        
    class Meta:
        model = Task
        fields = ['title', 'description', 'statustask', 'expire', 'label']
        widgets = {
            'expire': forms.DateInput(attrs={'type': 'date'})
        }