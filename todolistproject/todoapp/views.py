from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        context['count'] = context['task'].filter(complete=False).count()
        return context
    

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoapp/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task')

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')

class UserLoginView(LoginView):
    template_name = 'todoapp/login.html'
    field = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('task')
    