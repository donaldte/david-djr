from django.urls import path , include
from .views import register_user, get_user_profile ,  user_login, user_logout   , send_otp_phone  , change_password
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

urlpatterns = [
    #registerAuth
    path('', include(router.urls)),
    path('register/', views.register_user , name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login-with-otp'),
    path('api/change-password/', views.change_password, name='change-password'),
    path('send_otp_phone/', views.send_otp_phone, name='send_otp_phone'),
     path('forgot-password/', views.forgot_password, name='forgot_password'),

    
  

   #profile
    path('profile/', views.get_user_profile, name='get_profile'),
    path('profiles/', views.get_all_profile, name='get_all_profile'),
    # path('profile/update/', views.update_profile, name='update_profile'),
    path('api/reset-password/', views.reset_password, name='reset-password'),

]