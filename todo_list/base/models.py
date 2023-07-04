from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# Create your models here.
status_choice = (
    ('1', 'pending'),
    ('2', 'in progress'),
    ('3', 'complete'),
    ('4', 'cancel'),
) 
class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
class Label(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.tag

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    expire = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choice, default='1')
    label = models.ForeignKey(Label, on_delete=models.DO_NOTHING, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ['complete']