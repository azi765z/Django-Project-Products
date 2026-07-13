from rest_framework.permissions import BasePermission


class IsSellerRole(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        
        return user.role == "seller"
    
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True

        return False
    