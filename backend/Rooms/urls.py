from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  . import views



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('get-list/' , views.GetAllRooms),
    path('room/<int:pk>/' , views.GetRoomById),
    path('room/create/' , views.createRoomView),
    path('room/<int:pk>/update/' , views.updateRoom),
    path('room/<int:pk>/delete/' , views.deleteRoomView),
    path('room/<int:pk>/update/partiel/' , views.updatePartialRoom),
]