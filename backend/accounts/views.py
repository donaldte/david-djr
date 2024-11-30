from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes 
from .serialize import UserSerializer , VerifyAccountSerializer , ChangePasswordSerializer , VerifyCodeSerializer
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
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from datetime import timedelta
from django.utils import timezone
from accounts.models import Profile
from accounts.serialize import ProfileSerializer



User = get_user_model()

#api creation de compte
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
    
        


#api conexion user
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        exist_user = CustomUser.objects.filter(Q(username=username) | Q(email=username) | Q(telephone=username))
        if exist_user.exists():
            user = exist_user.first()
         
        if user:
            if user.check_password(password):
                token , created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid Credentials'} , status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Aucun user trouve'} , status=status.HTTP_404_NOT_FOUND)

    return Response({'error': 'Method non accepte'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



#api logout user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
           
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

#api forgot password envoit un email de renitialisation de mot de passe
@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    try:
        user  = CustomUser.objects.get(email=email)

        if user.reset_attempts >= 6:
            return Response({'error': 'Maximum de tentatives de réinitialisation atteint.'}, status=status.HTTP_400_BAD_REQUEST)
        
        token = get_random_string(5)
        user.code = token
        user.reset_code_expiration = timezone.now() + timedelta(minutes=5) #le code de renitialisatio expire apres 5 minutes
        user.reset_attempts += 1
        user.save()
 # Envoyer l'e-mail avec le lien de réinitialisation
        send_mail(
             'Réinitialisation de mot de passe',
            f'Votre code de réinitialisation est {token}',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return Response({'success': 'Code de réinitialisation envoyé'}, status=status.HTTP_200_OK)
    
    except CustomUser.DoesNotExist:
        return Response({'error': 'Email non trouvé'}, status=status.HTTP_404_NOT_FOUND)



#api de renitialisation de mot de passe
@api_view(['POST'])
def reset_password(request):
    code = request.data.get('code')
    new_password = request.data.get('new_password') 
    email= request.data.get('email')
# Récupérer l'utilisateur en fonction du code de réinitialisation
    try:
        user = CustomUser.objects.get(email=email)
         # Mettre à jour le mot de passe de l'utilisateur
       
        if user.code != code or user.reset_code_expiration < timezone.now():
            return Response({'error': 'Code de réinitialisation invalide ou expiré.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        return Response({'success': 'Mot de passe réinitialisé avec succès'}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Code de réinitialisation invalide'}, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):

    user = request.user
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')

# Vérifiez que le mot de passe actuel est correct

    if not user.check_password(current_password):
        return Response({'error': 'Le mot de passe actuel est incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()

    # Met à jour la session de l'utilisateur
    update_session_auth_hash(request, user)

    return Response({'success': 'Mot de passe changé avec succès.'}, status=status.HTTP_200_OK)
       

#Créeons une vue pour gérer l'URL de vérification
# @api_view(['POST'])
def verify_email(request , email):
    user = CustomUser.objects.get(pk=pk)
    if not user.email_verified:
        user.email_verified = True
        user.save()
        return redirect('http://localhost:8000/')
      # Replace with your desired redirect URL
    
#Récupère le profil de l'utilisateur authentifié et connecte.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)

    except Profile.DoesNotExist:
        return Response({"error":"Profil de l'utilisateur non trouve"} , status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfileSerializer(profile , many=False)
    return Response(serializer.data , status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_profile(request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)


#Met à jour les informations du profil de l'utilisateur.


    
       
#Supprime le compte de l'utilisateur.


