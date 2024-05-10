from rest_framework.permissions import BasePermission

from utils.utils import tokenValidation


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload and payload.get("is_manager") is True:
            return True
        else:
            False


class IsManager(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload and payload.get("is_manager") is True:
            return True
        else:
            False
