from rest_framework import permissions


class IsHRPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'hr'):
            return True
        else:
            return False


class AccessToInterview(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'hr'):
            return True
        elif hasattr(request.user, 'interviewer'):
            return True
        else:
            return False
