from django.contrib import admin

from user.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "email",
        "gender",
        "area",
        "total_project",
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
