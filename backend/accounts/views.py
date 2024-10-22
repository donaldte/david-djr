from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .serialize import UserSerializer , VerifyAccountSerializer , ChangePasswordSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from .utils import generate_otp, otp_send_mail , send_otp_phone
from rest_framework.decorators import api_view , APIView
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .helpers import send_otp_to_phone
from django.contrib.auth import update_session_auth_hash


User = get_user_model()


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)    
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            otp_send_mail(serializer.data['email'])
            return Response({
                'status' : 200,
                'message' : 'registration successfully check your email',
                'data':serializer.data
            })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

# accounts/views.py

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        otp = generate_otp()
        user.otp = otp
        user.save()

        otp_send_mail(email, otp)
        # send_otp_phone(phone_number, otp)

        return Response({'message': 'OTP has been sent to your email.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




@api_view(['POST'])
def verify_code_pour_se_loguer(request):
    username = request.data.get('username')
    code = request.data.get('code')

    try:
        user = User.objects.get(username=username)
        if user.code == code:
            return Response({'message': 'Code validé avec succès !'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Code invalide.'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'message': 'Utilisateur non trouvé.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data = request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request , user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#pour renitialiser le mot de passe il y'a deja un framework integre a django pour cela

@api_view(['POST'])
def ValidateOTP(self , request):
        data = request.data
        serialize = VerifyAccountSerializer(data=data)

        if serialize.is_valid():
            email = serialize.data['email']
            otp = serialize.data['otp']

            user = CustomUser.objects.filter(email = email)

            if not user.exists():
                return Response({
                    'status': 400 ,
                    'message':'something ',
                    'data':'Invalid email'
                })
        if user.first().otp !=otp:
             return Response({
                    'status': 400 ,
                    'message':'something ',
                    'data':'Invalid email'
                })
        user.first().is_active = True
        user.first().save()
        return Response({
                    'status': 400 ,
                    'message':'account verify ',
                    'data':{}
                }) 


#Créeons une vue pour gérer l'URL de vérification

def verify_email(request , pk):
    user = CustomUser.objects.get(pk=pk)
    if not user.email_verified:
        user.email_verified = True
        user.save()
        return redirect('http://localhost:8000/')  # Replace with your desired redirect URL
    

@api_view(['POST'])
def send_otp_phone(request):
    data = request.data


    if data.get('phone_number') is None:
        return Response({
            'status':400,
            'message':'key phone_number is required'
        })
    

    if data.get('password') is None:
        return Response({
            'status':400,
            'message':'key password is required'
        })
    

    user = User.objects.create(phone_number = data.get('phone_number'),
    otp = send_otp_to_phone(data.get('phone_number')
    ))
    user.set_password = data.get('set_password')
    user.save()

    return Response({'message': 'OTP send.'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def verify_otp_phnoe(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status':400,
            'message':'key phone_number is required'
        })
    

    if data.get('otp') is None:
        return Response({
            'status':400,
            'message':'key password is required'
        })
    try:
        user_object = CustomUser.objects.create(phone_number = data.get('phone_number')),
    except Exception as e:
        return Response({
            'status':400,
            'message':'invalid phone'
        })
    if user_object.otp == data.get('otp'):
        user_object.is_phone_verified = True
        user_object.save()
        
        return Response({
            'status':400,
            'message':'otp matched'
        })

    return Response({
            'status':400,
            'message':'invalid otp'
        })
    



