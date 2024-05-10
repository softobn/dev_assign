from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.token import CustomTokenView
from .views.profile import ProfileoView
from .views.project import ProjectListView
from .views.task import TaskListView


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
]
