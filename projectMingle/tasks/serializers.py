from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='project.owner.username')

    class Meta:
        model = Task
        fields = '__all__'
