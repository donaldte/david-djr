from django.urls import path

from .views import api_view
from .api.api import api_view_products


urlpatterns = [
    path('test/', api_view, name='api_test'),
    path('products/', api_view_products, name='api_products'),
    path('products/<int:pk>/', api_view_products, name='api_products_detail')
]