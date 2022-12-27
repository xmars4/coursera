from rest_framework import permissions


class AuthorizedManager(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name='Manager').exists() or user.is_superuser:
            return True
        else:
            return False
