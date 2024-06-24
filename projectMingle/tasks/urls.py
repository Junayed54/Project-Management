from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView
from comments.views import CommentListCreateAPIView
urlpatterns = [
    path('<uuid:project_id>/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('<uuid:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('<uuid:task_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
]
