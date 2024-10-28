from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Gestionnaires').exists()

class IsReceptionist(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Réceptionnistes').exists()


class IsPersonnalClean(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Personnel_nettoyage').exists()
    


