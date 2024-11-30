from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permet uniquement l'accès à l'admin
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsHotelManager(permissions.BasePermission):
    """
    Permet uniquement aux gestionnaires d'hôtel d'effectuer certaines actions
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='HotelManager').exists()

class IsClient(permissions.BasePermission):
    """
    Permet uniquement aux clients d'effectuer certaines actions
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Client').exists()

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permet à un utilisateur de modifier seulement ses propres ressources (comme une réservation).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
