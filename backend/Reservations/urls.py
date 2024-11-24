from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  . import views



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('get-list-reservations/' , views.getAllReservation),
    path('reservation/<int:pk>/' , views.getReservationById),
    path('reservation/create/' , views.CreateReservationView),
    path('reservation/<int:pk>/update/' , views.updateReservationView),
    path('reservation/<int:pk>/delete/' , views.deleteReservationView),
    path('reservation/<int:pk>/update/partiel/' , views.updatePartialReservation),
]