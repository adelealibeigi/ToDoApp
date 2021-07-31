from django.http import HttpResponseForbidden
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy
from .models import *


class TaskCreateView(CreateView):
    model = TaskList
    template_name = 'tasks/task_new.html'
    fields = ('title', 'description', 'category', 'priority', 'due_date', 'done',)


class TaskListView(ListView):
    model = TaskList
    template_name = 'tasks/task_list.html'


class TaskDetailView(DetailView):
    model = TaskList
    template_name = 'tasks/task_detail.html'


class TaskUpdateView(UpdateView):
    model = TaskList
    fields = ('title', 'description', 'category', 'priority', 'due_date', 'done',)
    template_name = 'tasks/task_update.html'


class TaskDeleteView(DeleteView):
    model = TaskList
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('ToDo:task_list')


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/category_new.html'
    fields = ('name',)


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_empty_category'] = Category.objects.not_empty_category()
        context['empty_category'] = Category.objects.empty_category()
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name',)
    template_name = 'categories/category_update.html'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    success_url = reverse_lazy('ToDo:category_list')

    def delete(self, *args, **kwargs):
        try:
            return super(CategoryDeleteView, self).delete(
                self, *args, **kwargs
            )
        except models.ProtectedError as e:
            return HttpResponseForbidden(
                "Can't delete, cause has task!"
            )


class Home(TemplateView):
    template_name = 'base.html'

