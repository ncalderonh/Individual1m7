from django.contrib import admin
from .models import Task, Label, Status

admin.site.register(Task)
admin.site.register(Label)
admin.site.register(Status)

# Register your models here.
