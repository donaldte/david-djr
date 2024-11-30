from django.shortcuts import render
from rest_framework import  status
from Rooms import SerializerRooms
from rest_framework.permissions import IsAuthenticated
from .models import Room
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import authentication
from .permissions import PermissionsAddRomm , CanUpdateRoomPermissions , AuthorRoomsPermissions
from rest_framework.exceptions import ValidationError
from Rooms.SerializerRooms import RoomSerializer

@api_view(['GET'])
def GetAllRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetRoomById(request , pk):
    room = get_object_or_404(Room , pk)
    serializer = SerializerRooms(room , many=False)
    return Response(serializer.data)

@permission_classes([ permissions.IsAuthenticated , PermissionsAddRomm])
@api_view(['POST'])
def createRoomView(request):
    serializer = RoomSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
      
@permission_classes([ permissions.IsAuthenticated , PermissionsAddRomm  , CanUpdateRoomPermissions])
@api_view(['PUT'])
def updateRoom(request , pk):
    room = get_object_or_404(Room , pk=pk)
    serializer = SerializerRooms(instance =room , data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@permission_classes([ permissions.IsAuthenticated , PermissionsAddRomm  , CanUpdateRoomPermissions])
@api_view(['PATCH'])
def updatePartialRoom(request , pk):
    room = get_object_or_404(Room , pk)
    serializer = SerializerRooms(instance=room, data=request.data , partial=True)

    try:
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data , status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail':'Erreur inattendue lors de la mise en jours de la chambre'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@permission_classes([ permissions.IsAuthenticated , PermissionsAddRomm  , AuthorRoomsPermissions])
@api_view(['DELETE'])
def deleteRoomView(request , pk):
    room = get_object_or_404(Room , pk=pk)

    if room.is_available !='Pas Occupe':
        return Response({'error': 'Cette chambre est occupe'} , status=status.HTTP_400_BAD_REQUEST)
    room.delete()
    return Response({'message':'Room successfully deleted'} , status=status.HTTP_204_NO_CONTENT)


