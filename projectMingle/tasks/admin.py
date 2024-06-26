from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'assigned_to', 'status', 'priority', 'due_date', 'created_at')
    list_filter = ('status', 'priority', 'created_at', 'due_date')
    search_fields = ('title', 'project__name', 'assigned_to__username')
    ordering = ('-created_at',)

# Alternative, simpler way to register without using @admin.register decorator:
# admin.site.register(Task, TaskAdmin)
