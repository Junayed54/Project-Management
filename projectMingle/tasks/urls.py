from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<uuid:project_id>/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('<uuid:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
]
