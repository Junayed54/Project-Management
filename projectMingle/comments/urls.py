from django.urls import path
from .views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<uuid:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]
