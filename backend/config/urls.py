from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        route="admin/",
        view=admin.site.urls,
        name="admin",
    ),
    path(
        route="api/manager/",
        view=include("manager_api.urls"),
        name="manager",
    ),
    path(
        route="api/user/",
        view=include("user_api.urls"),
        name="user",
    ),
    path(
        route="api/developer/",
        view=include("developer_api.urls"),
        name="developer",
    ),
]
