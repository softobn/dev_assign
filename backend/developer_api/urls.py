from django.urls import path

from .views.subtask import DeveloperCreateSubTaskView, DeveloperUpdateSubTaskView, DeveloperMarkSubTaskView


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
]
