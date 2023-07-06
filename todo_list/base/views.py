from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task, Label
from .forms import TaskForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

class LoginViewTodoList(LoginView):
    template_name = 'base/login.html'
    fields = '__all__' # Crea todos los campos para el formulario a partir del modelo predefinido de Django
    redirect_authenticated_user = True # Rediderciona si el login es exitoso
    def get_success_url(self):
        return reverse_lazy('profile')

class profile(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'profile.html'
    ordering = ['expire', 'create']

class TaskDetail(DetailView):
    model = Task
    context_object_name =  'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtener el contexto
        labels = Label.objects.all()  # Obtener todas las etiquetas
        context['labels'] = labels  # Agregar las etiquetas al contexto
        status = Task.statustask  # Obtener todos los estados del modelo Tarea
        context['status'] = status  # Agregar los estados al contexto
        return context


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtener el contexto
        labels = Label.objects.all()  # Obtener todas las etiquetas
        context['labels'] = labels  # Agregar las etiquetas al contexto
        status = Task.statustask  # Obtener todos los estados del modelo Tarea
        context['status'] = status  # Agregar los estados al contexto
        return context
    
    def get_success_url(self):
        return reverse_lazy('task', kwargs={'pk': self.object.pk})
    
class TaskDelete(DeleteView, LoginRequiredMixin):
    model = Task
    template_name = 'task_deleted.html'
    context_object_name = 'task'
    success_url =  reverse_lazy('profile')

class StatusChange (TemplateView):
        
    def post(self, request):
        task = Task.objects.get(id = request.POST.get('id'))
        task.complete = True
        task.save()
        return redirect('profile')