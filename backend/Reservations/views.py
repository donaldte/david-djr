from django.shortcuts import render
from Reservations.models import Reservation
from Rooms.models import Room
from rest_framework.decorators import api_view , permission_classes
from django.shortcuts import get_object_or_404
from Reservations import serializerReservation
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from rest_framework.exceptions import ValidationError
from rest_framework import permissions

@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def getAllReservation(request):
    reservations = Reservation.objects.all()
    serializer = serializerReservation(reservations , many=True)
    return Response(serializer.data)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def countAllResvation(request):
    reservations = Reservation.objects.all().count()
    serializer = serializerReservation(reservations , many=True)
    return Response(serializer.data)



@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def getReservationById(request , pk):
    reservation = get_object_or_404(Reservation , pk)
    serializer = serializerReservation(reservation , many=False)
    return Response(serializer.data)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['POST'])
def  CreateReservationView(request):
        room_id = request.data.get('room')
        check_in = request.data.get('start_date')   
        check_out = request.data.get('end_date')

        try:
            room = Room.objects.get(id=room_id)

            if not room.is_available:
                return Response({"detail": "Chambre non disponible"}, status=status.HTTP_400_BAD_REQUEST)

            # Créer la réservation
            reservation = Reservation(
                user=request.user,
                room=room,
                check_in=check_in,
                check_out=check_out
            )

            reservation.save()
            reservation.status = 'confirmee'
            reservation.save()
            return Response(serializerReservation(reservation).data , status=status.HTTP_201_CREATED)

        except Exception as e:
            # Mettre à jour la disponibilité de la chambre
            room.is_available = False
            room.save()

            return Response({"detail": "Réservation acceptée"}, status=status.HTTP_201_CREATED)

        except Room.DoesNotExist:
            return Response({"detail": "Chambre non trouvée"}, status=status.HTTP_404_NOT_FOUND)

#compter le nombre de reservation d'un utilisateur
@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def count_reservations(self, request , *args, **kwargs):
        period = request.query_params.get('period', 'month')  # Default to 'month'
        today = timezone.now().date()

        if period == 'month':
            start_date = today - timedelta(days=30)
        elif period == 'week':
            start_date = today - timedelta(days=7)
        elif period == 'year':
            start_date = today - timedelta(days=365)
        else:
            return Response({"detail": "Période invalide"}, status=status.HTTP_400_BAD_REQUEST)

        count = Reservation.objects.filter(utilisateur=request.user, date_debut__gte=start_date).count()
        return Response({"count": count}, status=status.HTTP_200_OK)

@permission_classes([ permissions.IsAuthenticated])
@api_view(['DELETE'])
def deleteReservationView(request , pk):
     reservation = get_object_or_404(Reservation , pk=pk)
     
     if reservation.status != 'annulee':
          return Response({'error':'Impossible de supprimer la reservation'} , status=status.HTTP_400_BAD_REQUEST)
     reservation.delete()
     return Response({'message' : 'Reservation supprime avec succes'} , status=status.HTTP_204_NO_CONTENT)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['PUT'])
def updateReservationView(request , pk):
     reservation = get_object_or_404(Reservation, pk=pk)
     serializer = serializerReservation(instance=reservation , data = request.data)
     if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
     return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@permission_classes([ permissions.IsAuthenticated])
@permission_classes([ permissions.IsAuthenticated])
@api_view(['PATCH'])
def updatePartialReservation(request , pk):
    reservation = get_object_or_404(Reservation , pk)
    serializer = serializerReservation(instance=reservation, data=request.data , partial=True)

    try:
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data , status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail':'Erreur inattendue lors de la mise en jours de la reservation'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
