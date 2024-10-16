from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import api_view
from .api.api import ProductMixinsApiView

urlpatterns = [
    path('test/', api_view, name='api_test'),
    # path('products/', api_view_products, name='api_products'),
    # path('products/<int:pk>/', api_view_products, name='api_products_detail')
    path('products/', ProductMixinsApiView.as_view(), name='api_products'),
    path('products/<int:pk>/', ProductMixinsApiView.as_view(), name='api_products'),
    path('login/', obtain_auth_token, name='api_login')
]