from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import api_view
from .api.api import ProductMixinsApiView
from  . import views
from .api.api import ProductMixinsApiView, api_view_products



urlpatterns = [
    path('test/', api_view, name='api_test'),
    path('products_1/', api_view_products, name='api_products_1'),
    path('products_1/<int:pk>/', api_view_products, name='api_products_detail'),
    path('products/', ProductMixinsApiView.as_view(), name='api_products'),
    path('products/<int:pk>/', ProductMixinsApiView.as_view(), name='api_products'),
    path('login/', obtain_auth_token, name='api_login')
]