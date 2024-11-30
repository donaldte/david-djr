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
from Reservations.serializerReservation import ReservationSerializer
from datetime import datetime
from Reservations.Permissions import IsHotelManager

@permission_classes([ permissions.IsAuthenticated , IsHotelManager])
@api_view(['GET'])
def getAllReservation(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations , many=True)
    return Response(serializer.data)


@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def countAllResvation(request):
    reservations = Reservation.objects.all().count()
    serializer = ReservationSerializer(reservations , many=True)
    return Response(serializer.data)



@permission_classes([ permissions.IsAuthenticated])
@api_view(['GET'])
def getReservationById(request , pk):
    reservation = get_object_or_404(Reservation , pk)
    serializer = serializerReservation(reservation , many=False)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])  # Utilisation du décorateur pour exiger une authentification
@api_view(['POST'])
def CreateReservationView(request):

    if not request.user.is_authenticated:
          return Response({"detail": "Vous devez être connecté pour effectuer une réservation."}, 
                         status=status.HTTP_401_UNAUTHORIZED)
       
    # Récupérer les données de la requête
    room_id = request.data.get('room')
    check_in = request.data.get('start_date')
    check_out = request.data.get('end_date')

    try:
        # Tentative de récupération de la chambre depuis l'ID
        room = Room.objects.get(id=room_id)

        # Vérifier si la chambre est disponible
        if not room.is_available:
            return Response({"detail": "Chambre non disponible"}, status=status.HTTP_400_BAD_REQUEST)
        

        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()  # Format : 'YYYY-MM-DD'
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
        except ValueError:
            return Response({"detail": "Le format des dates est incorrect. Utilisez 'YYYY-MM-DD'."}, 
                             status=status.HTTP_400_BAD_REQUEST)
        

        # Calcul du nombre de jours pour la réservation
        days = (check_out_date - check_in_date).days


        # Créer la réservation si la chambre est disponible
        reservation = Reservation(
            user=request.user,
            room=room,
            start_date=check_in_date,
            end_date=check_out_date,
            total_price=room.price * days,  # Exemple de calcul du prix total
            status='CONFIRMEE'  # Statut par défaut lors de la création de la réservation
        )

        # Enregistrer la réservation
        reservation.save()

        # Marquer la chambre comme non disponible
        room.is_available = False
        room.save()

        # Retourner une réponse avec les détails de la réservation
        return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)

    except Room.DoesNotExist:
        # Si la chambre n'existe pas, renvoyer une erreur 404
        return Response({"detail": "Chambre non trouvée"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        # Gérer d'autres erreurs génériques
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

@permission_classes([ permissions.IsAuthenticated , IsHotelManager])
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
     serializer = ReservationSerializer(instance=reservation , data = request.data)
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

    
