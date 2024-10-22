from rest_framework import serializers
from .models import CustomUser

class   UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password' , 'email_verified' , 'is_phone_verified']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

    def create_user(self , email , password=None):
        if not email :
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()


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
