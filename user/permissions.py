from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.role == "admin":
            return True

        elif request.user.role == "user":
            return False

        return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        return request.user.role == "admin"