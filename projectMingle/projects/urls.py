from django.urls import path
from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<uuid:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
]
