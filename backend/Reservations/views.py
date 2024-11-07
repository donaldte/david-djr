from django.shortcuts import render
from Reservations.models import Reservation
from Rooms.models import Room
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from Reservations import serializerReservation
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta

class UserReservationView(generics.ListAPIView):
       serializer_class = serializerReservation
       permission_classes = [IsAuthenticated]


       def get_queryset(self):
              user = self.request.user
              return Reservation.objects.filter(user=user)
              

class AcceptReservationView(generics.CreateAPIView):
    serializer_class = serializerReservation
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
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

            # Mettre à jour la disponibilité de la chambre
            room.is_available = False
            room.save()

            return Response({"detail": "Réservation acceptée"}, status=status.HTTP_201_CREATED)

        except Room.DoesNotExist:
            return Response({"detail": "Chambre non trouvée"}, status=status.HTTP_404_NOT_FOUND)


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