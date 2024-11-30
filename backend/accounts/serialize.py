from rest_framework import serializers
from .models import CustomUser
from accounts.models import Profile
import re

class   UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255 , write_only=True)
    confirm_password =serializers.CharField(style={'input_type': 'password'}, write_only=True)
    telephone = serializers.CharField(max_length=9)
    reset_code_expiration = serializers.DateTimeField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email','reset_code_expiration', 'password' , 'telephone','confirm_password', 'email_verified' , 'is_phone_verified' , ]

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            telephone=validated_data['telephone']
        )
#faire une verification du mail et password
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate_email(self , value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('this email is already use in the database')
        return value
    

    def validate_username(self , value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError('This username exists already')
        return value
    
    def validate(self, data):
        # Récupérer les deux mots de passe
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Vérifier si les mots de passe correspondent
        if password != confirm_password:
            raise serializers.ValidationError({"Error": "Les mots de passe ne correspondent pas."})

        return data  # Si tout est bon, retourner les données validées
    

    
    def validate_password(self , value):
        if len(value) < 8:
            raise serializers.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        if not re.search(r'[A-Z]', value):  # Vérifie la présence d'une majuscule
            raise serializers.ValidationError("Le mot de passe doit contenir au moins une lettre majuscule.")
        
        if not re.search(r'\d', value):  # Vérifie la présence d'un chiffre
            raise serializers.ValidationError("Le mot de passe doit contenir au moins un chiffre.")
        return value
        
        
    

    def set_password(self , raw_password):
        super().set_password(raw_password)
        self.reset_code = ''
        self.reset_code_expiration = None
        self.reset_attempts = 0
        self.save()



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user' , 'bio' , 'profile_picture' , 'region']


    def validate_bio(self , value):
        if len(value) > 500:
            raise serializers.ValidationError("La bio ne peut pas depasser 500 caracteres.")
        return value


    

    

class VerifyAccountSerializer(serializers.Serializer):

    class Meta: 
        model = CustomUser
        email = serializers.EmailField()
        otp = serializers.CharField()



class ChangePasswordSerializer(serializers.Serializer):
    class Meta: 
        model = CustomUser
        old_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True)


class ResetPasswordEqmailSerialier(serializers.Serializer):
    email = serializers.EmailField(required=True)


class VerifyCodeSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        username = serializers.CharField(required=True)
        code = serializers.CharField(required=True)

 