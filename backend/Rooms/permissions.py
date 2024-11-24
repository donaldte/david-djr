from rest_framework import permissions



class PermissionsAddRomm(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET" , "POST"]:
            if request.user.groups.filter(name = 'CAISSIERE').exists():
                return True
            
            if request.method == "GET":
                if request.user.groups.filter(name = 'RESPONSABLE').exists():
                    return True
                
            if request.method == "GET":
                if request.user.groups.filter(name = 'RECEPTIONNISTE').exists():
                    return True
                
            if request.method == "PUT":
                if request.user.groups.filter(name = 'RESPONSABLE').exists():
                    return True
                
            if request.method == "DELETE":
                if request.user.groups.filter(name = 'RESPONSABLE').exists():
                    return True
            else:
                return False
            


class CanUpdateRoomPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'
    
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user or request.user.role == 'admin'
    

class AuthorRoomsPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET" , "OPTIONS" , "HEAD"]:
            return True
        
        if request.method in ["PUT" , "PATCH" , "DELETE"]:
            if obj.user == request.user:
                return True
            return False
            
