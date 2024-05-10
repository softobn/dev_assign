from django.contrib import admin

from .models import ProjectModel


class ProjectAdmin(admin.ModelAdmin):
    def manager(self, obj):
        return obj.manager.email
    
    list_display = (
        "title",
        "manager",
        "planned_start",
        "planned_end",
        "deadline",
        "is_complete",
        "is_active",
    )
    list_display_links = (
        "title",
        "manager",
        "planned_start",
        "planned_end",
        "deadline",
    )
    search_fields = (
        "title",
        "manager",
        "planned_start",
        "planned_end",
        "deadline",
    )
    list_filter = [
        "is_complete",
        "is_active",
    ]
    list_per_page = 25


admin.site.register(ProjectModel, ProjectAdmin)
