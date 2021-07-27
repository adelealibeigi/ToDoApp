from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy
from .models import *


class TaskCreateView(CreateView):
    model = TaskList
    template_name = 'task_new.html'
    fields = ('title', 'description', 'category', 'priority', 'due_date', 'due_time',)


class TaskListView(ListView):
    model = TaskList
    template_name = 'task_list.html'


class TaskDetailView(DetailView):
    model = TaskList
    template_name = 'task_detail.html'

