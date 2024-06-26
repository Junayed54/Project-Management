from django.contrib import admin
from .models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'task', 'created_at')
    search_fields = ('content', 'user__username', 'task__name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)