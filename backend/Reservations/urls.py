from django.urls import path
from .views import UserReservationView, AcceptReservationView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reservations', AcceptReservationView.as_view(), basename='reservations')


urlpatterns = [
    path('reservations/accept/', AcceptReservationView.as_view(), name='accept-reservation'),
    # path('reservations/count/', AcceptReservationView.as_view({'get': 'count_reservations'}), name='count-reservations'),
]