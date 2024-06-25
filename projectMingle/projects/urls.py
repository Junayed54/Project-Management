from django.urls import path
from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView
from tasks.views import TaskListCreateAPIView
urlpatterns = [
    path('', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('<uuid:project_id>/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('<uuid:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
]
