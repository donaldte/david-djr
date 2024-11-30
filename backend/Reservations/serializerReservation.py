from rest_framework import serializers
from .models import Reservation
from Rooms import SerializerRooms
from .models import Hotel
from .models import CustomUser
from .models import Room


class ReservationSerializer(serializers.ModelSerializer):
    # hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    # user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    # room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    # status = serializers.ChoiceField(choices=Reservation.status)

    class Meta:
        model = Reservation
        fields = ['id', 'hotel', 'user', 'room', 'start_date', 'end_date', 'total_price', 'status']
        read_only_fields = ['id', 'total_price']


#Crée une nouvelle instance de réservation et calcule le prix total en fonction de la chambre et des dates choisies.
    # def create(self , validated_data):
    #     room = validated_data['room']
    #     start_date = validated_data['start_date']
    #     end_date = validated_data['end_date']

    #     # Calcul du prix total (exemple de calcul)

    #     number_of_day = (end_date - start_date).days
    #     total_price = room.price * number_of_day

    #     reservation = Reservation.objects.create(
    #         total_price = total_price,
    #          **validated_data
    #     )

    #     return reservation
    

    def update(self , instance , validated_data):
        instance.hotel = validated_data.get('hotel' , instance.hotel)
        instance.user = validated_data.get('user' , instance.user)
        instance.room = validated_data.get('room' , instance.room)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.status = validated_data.get('status', instance.status)


        # Recalcule le prix si la chambre ou les dates changent

        if 'room' in validated_data or 'start_date' in validated_data or 'end_date' in validated_data:
            room = instance.room
            start_date = instance.start_date
            end_date = instance.end_date
            number_of_days = (end_date - start_date).days
            instance.total_price = room.price * number_of_days 


        instance.save()
        return instance

#valider que les dates de reservation sont valides la date de fin doit etre apres la date de debut
    def validate(self , data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("La date de fin doit etre superieur a la date de debut")
        return data







