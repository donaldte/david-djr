from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  . import views



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('get-list-reservations/' , views.getAllReservation),
    path('reservation/<int:pk>/' , views.getReservationById),
    path('reservation/create/' , views.CreateReservationView),
    path('reservation/update/<int:pk>/' , views.updateReservationView),
    path('reservation/delete/<int:pk>/' , views.deleteReservationView),
    path('reservation/update/partiel/<int:pk>/' , views.updatePartialReservation),
    path('reservation/count/' , views.countAllResvation),
]