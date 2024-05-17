from django.urls import path

from .views.project import ManagerCreateProjectView
from .views.project import ManagerUpdateProjectView
from .views.project import ManagerMarkprojectView
from .views.task import ManagerCreateTaskView
from .views.task import ManagerUpdateTaskView


urlpatterns = [
    # ttp://localhost:8000/api/manager/project-create/
    path(
        route="project-create/",
        view=ManagerCreateProjectView.as_view(),
        name="manager_project_create",
    ),
    # http://localhost:8000/api/manager/project-update/
    path(
        route="project-update/",
        view=ManagerUpdateProjectView.as_view(),
        name="manager_project_update",
    ),
    # http://localhost:8000/api/manager/task-create/
    path(
        route="task-create/",
        view=ManagerCreateTaskView.as_view(),
        name="manager_task_create",
    ),
    # http://localhost:8000/api/manager/task-update/
    path(
        route="task-update/",
        view=ManagerUpdateTaskView.as_view(),
        name="manager_task_update",
    ),
    # http://localhost:8000/api/manager/mark-project/
    path(
        route="mark-project/",
        view=ManagerMarkprojectView.as_view(),
        name="manager_mark_project",
    ),
]
