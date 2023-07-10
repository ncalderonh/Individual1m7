from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Task, Label, Category, Status
from .forms import TaskForm
from datetime import datetime

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

    def get_queryset(self): # Acá ordeno las querys para ordenar las tareas y filtrar para obtener sólo las tareas del usuario logueado
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count1'] = context['tasks'].filter(complete=True, user=self.request.user).count()
        context['count2'] = context['tasks'].filter(statustask=1 ,user=self.request.user).count()
        context['count3'] = context['tasks'].filter(statustask=2, user=self.request.user).count()
        context['count4'] = context['tasks'].filter(expire__lt=datetime.now(), user=self.request.user).count()

        search_input = self.request.GET.get('search-area') or '' #Esto indica que la busqueda puede tener un valor o dejarse ne blanco ('')
        if search_input:
            context ['tasks'] = context ['tasks'].filter(title__icontains = search_input) # Acá busca por título
            context['search_input'] = search_input
        return context

class TaskDetail(DetailView):
    model = Task
    context_object_name =  'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtener el contexto
        labels = Label.objects.all()  # Obtener todas las etiquetas
        context['labels'] = labels  # Agregar las etiquetas al contexto
        categories = Category.objects.all()  # Obtener todas las etiquetas
        context['categories'] = categories  # Agregar las etiquetas al contexto
        status = Task.statustask  # Obtener todos los estados del modelo Tarea
        context['status'] = status  # Agregar los estados al contexto
        user = User.objects.all()
        context['users'] = user
        context['actualuser'] = self.request.user
        return context

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtener el contexto
        labels = Label.objects.all()  # Obtener todas las etiquetas
        context['labels'] = labels  # Agregar las etiquetas al contexto
        categories = Category.objects.all()  # Obtener todas las etiquetas
        context['categories'] = categories  # Agregar las etiquetas al contexto
        status = Task.statustask  # Obtener todos los estados del modelo Tarea
        context['status'] = status  # Agregar los estados al contexto
        user = User.objects.all()
        context['users'] = user
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
        task_id = request.POST.get('id')
        task = Task.objects.get(id=task_id)

        completed_status = Status.objects.get(name="complete")
        task.statustask = completed_status
        
        # Establecer complete como True
        task.complete = True
        
        task.save()
        return redirect('profile')