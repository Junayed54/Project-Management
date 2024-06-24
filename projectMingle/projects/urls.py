from django.urls import path
from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('<uuid:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
]
