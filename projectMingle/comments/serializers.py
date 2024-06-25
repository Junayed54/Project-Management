from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ReadOnlyField(source='task.assigned_to.username')

    class Meta:
        model = Comment
        fields = '__all__'
