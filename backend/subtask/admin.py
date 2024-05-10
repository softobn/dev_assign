from django.contrib import admin

from .models import SubTaskModel


class SubTaskAdmin(admin.ModelAdmin):
    def task(self, obj):
        return obj.task.title
    
    list_display = (
        "title",
        "task",
        "deadline",
        "is_complete",
        "is_active",
    )
    list_display_links = (
        "title",
        "task",
        "deadline",
    )
    search_fields = (
        "title",
        "task",
        "deadline",
    )
    list_filter = [
        "is_complete",
        "is_active",
    ]
    list_per_page = 25


admin.site.register(SubTaskModel, SubTaskAdmin)
