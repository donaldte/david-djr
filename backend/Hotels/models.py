from django.db import models
from rest_framework import filters
from django_filters import rest_framework as django_filters


class Hotel(models.Model):
        name = models.CharField(max_length=100)
        adress = models.CharField(max_length=100)
        description = models.CharField(max_length=50)
        phone_number = models.CharField(max_length=50)
        email = models.EmailField()
        city = models.CharField(max_length=100 , null=True, blank=True)
        # img = models.ImageField(upload_to="hotel/" , blank=True , null=True)
        notation = models.FloatField(default=1)
        price_per_night = models.DecimalField(max_digits=10, decimal_places=2 , null=True , blank=True)

        def __str__(self):
            return self.description

#permet de filtrer les hotels par name , par adress, par min_price , par notation
class HotelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    adress = django_filters.CharFilter(lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')
    notation = django_filters.NumberFilter(field_name='stars', lookup_expr='exact')

    class Meta:
        model = Hotel
        fields = ['name', 'adress', 'min_price', 'max_price', 'notation']
