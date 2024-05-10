from django.contrib import admin

from .models import CommentModel


class CommentAdmin(admin.ModelAdmin):
    def user(self, obj):
        return obj.user.email
    
    def task(self, obj):
        return obj.task.title
    
    def subtask(self, obj):
        return obj.subtask.title
    
    list_display = (
        "user",
        "reply",
        "task",
        "subtask",
        "is_active",
    )
    list_display_links = (
        "user",
        "reply",
        "task",
    )
    search_fields = (
        "user",
        "reply",
        "task",
    )
    list_filter = [
        "is_active",
    ]
    list_per_page = 25


admin.site.register(CommentModel, CommentAdmin)
