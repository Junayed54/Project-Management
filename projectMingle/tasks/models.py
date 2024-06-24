import uuid
from django.db import models
from projects.models import Project
from users.models import User

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=(('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')))
    priority = models.CharField(max_length=50, choices=(('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')))
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()