from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render
from Hotels.models import Hotel , HotelFilter
from Rooms.models import Room
from rest_framework.decorators import api_view , permission_classes
from django.shortcuts import get_object_or_404
from Hotels import serializerHotels
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from rest_framework import filters
from django_filters import rest_framework as django_filters
from .serializerHotels import HotelSerializer



#affiche les hotels avec la possibilte de filtrer en fonction des criteres specifiques
@permission_classes([IsAuthenticated])  # Permet d'exiger que l'utilisateur soit authentifié
@api_view(['GET'])  # La vue accepte seulement les requêtes GET
def getAllHotels(request):
    # Appliquer les filtres aux hôtels
    queryset = Hotel.objects.all()
    hotel_filter = HotelFilter(request.GET, queryset=queryset)
    
    if hotel_filter.is_valid():  # Si les filtres sont valides
        queryset = hotel_filter.qs
    
    # Ordonnancement par prix (par défaut)
    ordering = request.GET.get('ordering', 'price_per_night')  # Récupérer un paramètre d'ordre s'il existe
    queryset = queryset.order_by(ordering)

    #Ordonnacement par ville
    
    
    # Sérialisation des hôtels
    serializer = HotelSerializer(queryset, many=True)
    
    return Response(serializer.data)



@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def getHotelById(request , pk):
    hotels = get_object_or_404(Hotel , pk)
    serializer = serializerHotels(hotels , many=False)
    return Response(serializer.data)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['POST'])
def  CreateHotelsView(request):
        name = request.data.get('name')
        adress = request.data.get('adress')   
        description = request.data.get('description')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')

        
            # Créer le commentaire
        hotels = Hotel(
                user=request.user,
                name=name,
                adress=adress,
                description=description,
                phone_number=phone_number,
                email=email
            )

        hotels.save()
        return Response(serializerHotels(hotels).data , status=status.HTTP_201_CREATED)

        

@permission_classes([ permissions.IsAuthenticated])
@api_view(['DELETE'])
def deleteHotelView(request , pk):
     hotels = get_object_or_404(Hotel , pk=pk)
     
     if hotels.status != 'annulee':
          return Response({'error':'Impossible de supprimer la reservation'} , status=status.HTTP_400_BAD_REQUEST)
     hotels.delete()
     return Response({'message' : 'Reservation supprime avec succes'} , status=status.HTTP_204_NO_CONTENT)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['PUT'])
def updateHotelsView(request , pk):
     hotels = get_object_or_404(Hotel, pk=pk)
     serializer = serializerHotels(instance=hotels , data = request.data)
     if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
     return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@permission_classes([ permissions.IsAuthenticated])
@api_view(['PATCH'])
def updatePartialHotels(request , pk):
    hotels = get_object_or_404(Hotel , pk=pk)
    serializer = serializerHotels(instance=hotels, data=request.data , partial=True)

    try:
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data , status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail':'Erreur inattendue lors de la mise en jours hotel'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)



     
     

    


