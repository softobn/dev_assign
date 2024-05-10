from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.token import CustomTokenView
from .views.profile import ProfileoView
from .views.project import ProjectListView, ProjectDoneView, ProjectInprocessView, ProjectCreatedCountView
from .views.task import TaskListView
from .views.subtask import SubTaskListView
from .views.comment import CommentCreateView, CommentListView
from .views.developer import DeveloperRegisterView, DeveloperListView, DeveloperCountView


urlpatterns = [
    # ttp://localhost:8000/api/user/login/
    path(
        route="login/",
        view=CustomTokenView.as_view(),
        name="login",
    ),
    # http://localhost:8000/api/user/refresh/
    path(
        route="refresh/",
        view=TokenRefreshView.as_view(),
        name="refresh",
    ),
    # http://localhost:8000/api/user/profile/
    path(
        route="profile/",
        view=ProfileoView.as_view(),
        name="profile",
    ),
    # http://localhost:8000/api/user/project-list/
    path(
        route="project-list/",
        view=ProjectListView.as_view(),
        name="project_list",
    ),
    # http://localhost:8000/api/user/task-list/
    path(
        route="task-list/",
        view=TaskListView.as_view(),
        name="task_list",
    ),
    # http://localhost:8000/api/user/subtask-list/
    path(
        route="subtask-list/",
        view=SubTaskListView.as_view(),
        name="subtask_list",
    ),
    # http://localhost:8000/api/user/comment-create/
    path(
        route="comment-create/",
        view=CommentCreateView.as_view(),
        name="comment_create",
    ),
    # http://localhost:8000/api/user/comment-list/
    path(
        route="comment-list/",
        view=CommentListView.as_view(),
        name="comment_list",
    ),
    # http://localhost:8000/api/user/developer-register/
    path(
        route="developer-register/",
        view=DeveloperRegisterView.as_view(),
        name="developer_register",
    ),
    # http://localhost:8000/api/user/developer-list/
    path(
        route="developer-list/",
        view=DeveloperListView.as_view(),
        name="developer_list",
    ),
    # http://localhost:8000/api/user/project-done/
    path(
        route="project-done/",
        view=ProjectDoneView.as_view(),
        name="project_done",
    ),
    # http://localhost:8000/api/user/project-inprocess/
    path(
        route="project-inprocess/",
        view=ProjectInprocessView.as_view(),
        name="project_inprocess",
    ),
    # http://localhost:8000/api/user/project-created/
    path(
        route="project-created/",
        view=ProjectCreatedCountView.as_view(),
        name="project_created",
    ),
    # http://localhost:8000/api/user/developer-count/
    path(
        route="developer-count/",
        view=DeveloperCountView.as_view(),
        name="developer_count",
    ),
]
