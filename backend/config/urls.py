from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        route="admin/",
        view=admin.site.urls,
        name="admin",
    ),
    path(
        route="api/v1/manager/",
        view=include("manager_api.urls"),
        name="manager",
    ),
]
