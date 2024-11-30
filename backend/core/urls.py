
from django.contrib import admin
from django.urls import path, include
# from rest_framework.views import verify_email


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from django.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from products.api.accounts.api import ProfileViewApi, RegisterViewApi


schema_view = get_schema_view(
   openapi.Info(
      title="API BOOKING HOTELS",
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
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   
]

# from rest_registration.api.views import login, change_password, reset_password, send_reset_password_link

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/accounts/', include('accounts.urls')),
   path('api/reservations/', include('Reservations.urls')),
   path('api/commentaires/', include('Commentaires.urls')),
   path('api/payements/', include('Payements.urls')),
   path('api/rooms/', include('Rooms.urls')),
   path('api/hotels/', include('Hotels.urls')),
   
]


urlpatterns = urlpatterns + urlpatterns_doc

