from rest_framework import serializers
from .models import CustomUser

class   UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255 , write_only=True)
    password2 =serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password' ,'password2', 'email_verified' , 'is_phone_verified']
        

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
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
    
    def validate_two_password(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Error": "Password Does not match"})
        return password

    

    

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
 