from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
        
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'statustask', 'expire', 'label', 'comment', 'category']
        widgets = {
            'expire': forms.DateInput(attrs={'type': 'date'})
        }

# class comment(TaskForm):
#     class Meta(TaskForm.Meta):
#         fields = ['comment']