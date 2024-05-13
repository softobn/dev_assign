from django.contrib import admin
from django.utils.html import mark_safe

from user.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    def display_picture(self, obj):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % obj.profile_picture)
    display_picture.allow_tags = True
    display_picture.short_description = 'Picture'

    list_display = (
        "phone_number",
        "email",
        "gender",
        "area",
        "total_project",
        "display_picture",
        "is_developer",
        "is_manager",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "phone_number",
        "email",
        "gender",
        "area",
        "total_project",
    )
    search_fields = (
        "phone_number",
        "email",
        "gender",
        "area",
        "total_project",
    )
    list_filter = [
        "is_developer",
        "is_manager",
        "is_active",
    ]
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
