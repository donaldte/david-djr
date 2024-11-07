
from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from products.api.accounts.api import RegisterViewApi


schema_view = get_schema_view(
   openapi.Info(
      title="DAVID API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns_doc = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]

from rest_registration.api.views import login, change_password, reset_password, send_reset_password_link 

urlpatterns = [
    #path('accounts/', include('rest_registration.api.urls')),
    path('accounts/login/', login, name='login'),
    path('accounts/registration/', RegisterViewApi.as_view(), name='registration'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
]


urlpatterns = urlpatterns + urlpatterns_doc

