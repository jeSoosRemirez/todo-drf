from django.urls import path
from todo_app.views import TaskListView, TaskCreateView, TaskDetailView, api_root
from rest_framework.urlpatterns import format_suffix_patterns


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
])
