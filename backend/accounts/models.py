from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=9 , null=True , blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    code = models.CharField(max_length=5 , null=False , blank=True) 
    reset_code_expiration = models.DateTimeField(blank=True, null=True)
    reset_attempts = models.IntegerField(default=0)
    reset_code = models.CharField(max_length=20, blank=True, null=True)

    #la variable code va permettre a l'utilisateur de se connecter via un code a 5 chiffres
    


    def __str__(self):
        return self.username
    


class Profile(models.Model):
        user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
        bio = models.TextField(blank=True , null=True)
        # profile_picture = models.ImageField(upload_to='profile_pics' , blank=True, null=True)
        region = models.CharField(max_length=30 , blank=True , null=True)


        class Meta:
            ordering = ['region']

        def __str__(self) :
            return f"{self.bio} {self.region}"
