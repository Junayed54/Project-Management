from rest_framework import generics, permissions
from .models import Comment, Task
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        task = get_object_or_404(Task, id=task_id)
        serializer.save(task=task, user=self.request.user)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
