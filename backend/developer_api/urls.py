from django.urls import path

from .views.subtask import DeveloperCreateSubTaskView, DeveloperUpdateSubTaskView, DeveloperMarkSubTaskView
from .views.task import DeveloperMarkTaskView


urlpatterns = [
    # ttp://localhost:8000/api/developer/subtask-create/
    path(
        route="subtask-create/",
        view=DeveloperCreateSubTaskView.as_view(),
        name="developer_subtask_create",
    ),
    # http://localhost:8000/api/developer/subtask-update/
    path(
        route="subtask-update/",
        view=DeveloperUpdateSubTaskView.as_view(),
        name="developer_subtask_update",
    ),
    # http://localhost:8000/api/developer/subtask-mark/
    path(
        route="subtask-mark/",
        view=DeveloperMarkSubTaskView.as_view(),
        name="developer_subtask_mark",
    ),
    # http://localhost:8000/api/developer/task-mark/
    path(
        route="task-mark/",
        view=DeveloperMarkTaskView.as_view(),
        name="developer_task_mark",
    ),
]
