from django.contrib import admin

from .models import OnTaskModel


class OnTaskAdmin(admin.ModelAdmin):
    def project(self, obj):
        return obj.project.title
    
    def developer(self, obj):
        return obj.developer.email
    
    list_display = (
        "project",
        "developer",
        "is_active",
    )
    list_display_links = (
        "project",
        "developer",
    )
    search_fields = (
        "project",
        "developer",
    )
    list_filter = [
        "is_active",
    ]
    list_per_page = 25


admin.site.register(OnTaskModel, OnTaskAdmin)
