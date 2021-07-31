from django.urls import path
from .views import *

app_name = 'ToDo'
urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('task/new/', TaskCreateView.as_view(), name='task_new'),
    path('task/list/', TaskListView.as_view(), name='task_list'),
    path('task/<str:slug>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<str:slug>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<str:slug>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('category/new/', CategoryCreateView.as_view(), name='category_new'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

]
