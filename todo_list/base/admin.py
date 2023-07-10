from django.contrib import admin
from .models import Task, Label, Status, Category

admin.site.register(Task)
admin.site.register(Label)
admin.site.register(Status)
admin.site.register(Category)

# Register your models here.
