from django.urls import path

from .views.project import ManagerCreateProjectView
from .views.project import ManagerUpdateProjectView


urlpatterns = [
    # ttp://localhost:8000/api/v1/manager/project-create/
    path(
        route="project-create/",
        view=ManagerCreateProjectView.as_view(),
        name="manager_project_create",
    ),
    # http://localhost:8000/api/v1/manager/project-update/
    path(
        route="project-update/",
        view=ManagerUpdateProjectView.as_view(),
        name="manager_project_update",
    ),
]
