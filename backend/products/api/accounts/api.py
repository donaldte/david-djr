from rest_registration.api.views import register
from rest_registration.api.views.register import RegisterView
from rest_registration.api.views.profile import ProfileView
from rest_framework.serializers import Serializer
from typing import Type



class RegisterViewApi(RegisterView):
    
   
   def get_serializer_class(self) -> Type[Serializer]:
       return "mon serializer ici" 
    
    
class ProfileViewApi(ProfileView):
   
   permission_classes = []
    
   def get_serializer_class(self) -> Type[Serializer]:
      return "mon serializer ici"    