from rest_framework.permissions import DjangoModelPermissions
from rest_framework import permissions

class IsOwnerOrReadOnly(DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
    
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.method in permissions.SAFE_METHODS:
            return True
        

class CanCreateProductPremissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user = request.user 
            if user.has_perm('products.add_product'):
                return True
        return False     
            