from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    code = models.CharField(max_length=5 , null=False , blank=True) 

    #la variable code va permettre a l'utilisateur de se connecter via un code a 5 chiffres
    


    def __str__(self):
        return self.username