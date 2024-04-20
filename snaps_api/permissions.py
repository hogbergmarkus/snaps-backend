from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    This code was directly taken from the drf_api project:
    https://github.com/Code-Institute-Solutions/drf-api/blob/025406b0a0fb365a1931747b596c33fd3ba2a6dc/drf_api/permissions.py
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.profile_owner == request.user
