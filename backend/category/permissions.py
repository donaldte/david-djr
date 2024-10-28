from rest_framework import permissions

class IsStaffPermission(permissions.DjangoModelPermissions):
    
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            if user.has_perm('category.add_Product'):   #(add , delete , view , change) , #app_name.perm_name_name_model
                return True
            if user.has_perm('product.change_product'):
                return True
            if user.has_perm('product.delete_product'):
                return True
            if user.has_perm('product.view_product'):
                return True
            
        return False
    
#mes groupes d'utilisateurs : 
# Administrateurs : Accès complet à toutes les fonctionnalités de l'application.
#Gestionnaires d'hôtel : (Gestion des réservations.Gestion des chambres (ajouter, modifier, supprimer).Gestion des clients.)
#Réceptionnistes(Accès aux réservations et à la gestion des clients. Check-in et check-out des clients.Accès limité à la gestion des chambres.)
#Personnel de nettoyage Accès aux informations sur les chambres.Mise à jour de l'état des chambres (nettoyée, occupée, etc.).
#Clients Consultation des informations sur les chambres.Réservation de chambres.Gestion de leurs propres réservations. 






    


class MyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET" , "POST"]:
            if request.user.groups.filter(name = 'Vendeur').exists():
                return True
            
            if request.method == "GET":
                if request.user.groups.filter(name = 'Acheteur').exists():
                    return True
                
            if request.method == "GET":
                if request.user.groups.filter(name = 'Livreur').exists():
                    return True
                
            if request.method == "PUT":
                if request.user.groups.filter(name = 'Vendeur').exists():
                    return True
                
            if request.method == "DELETE":
                if request.user.groups.filter(name = 'Vendeur').exists():
                    return True
            else:
                return False
            

class AuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "OPTIONS" , "HEAD"]:
            return True
        if obj.vendeur == request.user:
            return True
        return False