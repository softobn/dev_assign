from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.token import CustomTokenView
from .views.profile import ProfileoView


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
]
