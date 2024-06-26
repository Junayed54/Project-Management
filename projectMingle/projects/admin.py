from django.contrib import admin
from .models import Project, ProjectMember

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner', 'created_at')
    search_fields = ('name', 'description', 'owner__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'role')
    search_fields = ('project__name', 'user__username', 'role')
    list_filter = ('role',)
    ordering = ('project', 'user')

# Alternative, simpler way to register without using @admin.register decorator:
# admin.site.register(Project, ProjectAdmin)
# admin.site.register(ProjectMember, ProjectMemberAdmin)
