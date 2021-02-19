from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'user') and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return hasattr(request, 'user') and request.user.is_superuser


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'user') and request.user.is_client

    def has_object_permission(self, request, view, obj):
        return hasattr(request, 'user') and request.user.is_client


class IsSalesman(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'user') and request.user.is_salesman

    def has_object_permission(self, request, view, obj):
        return hasattr(request, 'user') and request.user.is_salesman
