from django.urls import path , include
from .views import register_user, user_login, user_logout   , send_otp_phone  , change_password
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_user , name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login-with-otp'),
    # path('validate-otp/', views.ValidateOTP, name='validate-otp'),
    path('send_otp_phone/', views.send_otp_phone, name='send_otp_phone'),
    # path('verify-code/', views.verify_code_pour_se_loguer, name='verify-code'),
    path('api/change-password/', views.change_password, name='change-password'),
    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('api/verify_otp_phnoe/' , views.verify_otp_phone, name='verify_otp_phnoe'),
    # path('verify_email/<int:pk>/', verify_email, name='verify_email'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('profile/', views.get_profile, name='get_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('api/reset-password/', views.reset_password, name='reset-password'),

]