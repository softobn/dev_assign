from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.token import CustomTokenView


urlpatterns = [
    # ttp://localhost:8000/api/v1/user/login/
    path(
        route="login/",
        view=CustomTokenView.as_view(),
        name="login",
    ),
    # http://localhost:8000/api/v1/user/refresh/
    path(
        route="refresh/",
        view=TokenRefreshView.as_view(),
        name="refresh",
    ),
]
