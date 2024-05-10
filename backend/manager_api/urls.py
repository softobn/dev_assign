from django.urls import path

from .views.project import ManagerCreateProjectView
from .views.project import ManagerUpdateProjectView
from .views.task import ManagerCreateTaskView
from .views.task import ManagerUpdateTaskView


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
    # http://localhost:8000/api/v1/manager/task-create/
    path(
        route="task-create/",
        view=ManagerCreateTaskView.as_view(),
        name="manager_task_create",
    ),
    # http://localhost:8000/api/v1/manager/task-update/
    path(
        route="task-update/",
        view=ManagerUpdateTaskView.as_view(),
        name="manager_task_update",
    ),
]
