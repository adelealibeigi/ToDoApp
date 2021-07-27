from django.urls import path
from .views import *

app_name = 'ToDo'
urlpatterns = [
    path('new/',TaskCreateView.as_view(), name='task_new'),
    path('',TaskListView.as_view(), name='task_list'),
    # path('<slug:slug>/',TaskDetailView.as_view(), name='task_detail'),
    path('task/<str:slug>/',TaskDetailView.as_view(), name='task_detail'),
    # path('task/<int:id>/',TaskDetailView.as_view(), name='task_detail'),
    # path('task/<slug:slug>/',TaskDetailView.as_view(), name='task_detail'),
]