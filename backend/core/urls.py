
from django.contrib import admin
from django.urls import path, include
# from rest_framework.views import verify_email
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
    path('api/accounts/', include('accounts.urls')),
    # path('api/category/' , include('category.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
