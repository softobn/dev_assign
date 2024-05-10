from django.contrib import admin

from .models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    def project(self, obj):
        return obj.project.title
    
    list_display = (
        "title",
        "project",
        "deadline",
        "is_complete",
        "is_active",
    )
    list_display_links = (
        "title",
        "project",
        "deadline",
    )
    search_fields = (
        "title",
        "project",
        "deadline",
    )
    list_filter = [
        "is_complete",
        "is_active",
    ]
    list_per_page = 25


admin.site.register(TaskModel, TaskAdmin)
