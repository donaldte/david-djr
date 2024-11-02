from django.shortcuts import render
from Reservations.models import Reservation
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from Reservations import serializerReservation


@api_view(['GET'])
def numOfDays(request, pk=None, *args, **kwargs):
              if request.method == 'GET':
                    if pk:
                      reservation = get_object_or_404(Reservation , pk=pk)
                      serializer = serializerReservation(reservation , pk)
                      totalDays = 0
              reservations = Reservation.objects.filter(guest=self)
              for reservation in reservations:
                    day = reservation.end_date - reservation.start_date
                    totalDays +=int(day.days)
                    return totalDays
              
