from django.shortcuts import render

from django.shortcuts import render
from Commentaires.models import Commentaire
from Rooms.models import Room
from rest_framework.decorators import api_view , permission_classes
from django.shortcuts import get_object_or_404
from Commentaires import serializersCommentaire
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from rest_framework.exceptions import ValidationError
from rest_framework import permissions

@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def getAllCommentaires(request):
    commentaires = Commentaire.objects.all()
    serializer = serializersCommentaire(commentaires , many=True)
    return Response(serializer.data)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def countAllCommentairesbyrooms(request):
    commentaires = Commentaire.objects.all().count()
    serializer = serializersCommentaire(commentaires , many=True)
    return Response(serializer.data)



@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def getCommentaireById(request , pk):
    commentaires = get_object_or_404(Commentaire , pk)
    serializer = serializersCommentaire(commentaires , many=False)
    return Response(serializer.data)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['POST'])
def  CreateCommentaireView(request):
        room = request.data.get('room')
        notation = request.data.get('notation')   
        commentaire = request.data.get('commentaire')
        create_date = request.data.get('create_date')

        
            # Créer le commentaire
        commentaire = Commentaire(
                user=request.user,
                room=room,
                notation=notation,
                commentaire=commentaire
            )

        commentaire.save()

        return Response(serializersCommentaire(commentaire).data , status=status.HTTP_201_CREATED)

        

@permission_classes([ permissions.IsAuthenticated])
@api_view(['DELETE'])
def deleteCommentaireView(request , pk):
     commentaires = get_object_or_404(Commentaire , pk=pk)
     
     if commentaires.status != 'annulee':
          return Response({'error':'Impossible de supprimer la reservation'} , status=status.HTTP_400_BAD_REQUEST)
     commentaires.delete()
     return Response({'message' : 'Reservation supprime avec succes'} , status=status.HTTP_204_NO_CONTENT)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['PUT'])
def updateCommentaireView(request , pk):
     commentaires = get_object_or_404(Commentaire, pk=pk)
     serializer = serializersCommentaire(instance=commentaires , data = request.data)
     if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
     return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@permission_classes([ permissions.IsAuthenticated])
@permission_classes([ permissions.IsAuthenticate])
@api_view(['PATCH'])
def updatePartialCommentaireView(request , pk):
    commentaires = get_object_or_404(Commentaire , pk)
    serializer = serializersCommentaire(instance=commentaires, data=request.data , partial=True)

    try:
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data , status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail':'Erreur inattendue lors de la mise en jours de la reservation'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

