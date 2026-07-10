from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"
    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        
        elif request.user.role == 'user':
            return obj.user == request.user

