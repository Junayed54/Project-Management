from django.urls import path
from .views import UserRegisterAPIView, UserLoginAPIView, UserDetailsAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('<uuid:pk>/', UserDetailsAPIView.as_view(), name='user-detail'),
]
