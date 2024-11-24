from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  . import views



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('get-list-hotels/' , views.getAllHotels),
    path('hotel/<int:pk>/' , views.getHotelById),
    path('hotel/create/' , views.CreateHotelsView),
    path('hotel/<int:pk>/update/' , views.updateHotelsView),
    path('hotel/<int:pk>/delete/' , views.deleteHotelView),
    path('hotel/<int:pk>/update/partiel/' , views.updatePartialHotels),
]