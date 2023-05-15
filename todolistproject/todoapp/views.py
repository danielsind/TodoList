from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from . import Task
# Create your views here.
class TaskList(ListView):
    model = Task
