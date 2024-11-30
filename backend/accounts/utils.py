import random
import string
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from .models import CustomUser

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for  _ in range(length))
    return otp

  
def otp_send_mail(email):
    subject = 'Votre code OTP'
    otp = generate_otp()
    message = f'Votre OTP est : {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject , message , from_email , recipient_list)
    user_object = CustomUser.objects.get(email=email)
    user_object.otp = otp
    user_object.save()


    

def send_otp_phone(phone_number , otp):
    account_sid = 'your_account_sid'  # Replace with your Twilio account SID
    auth_token = 'your_auth_token'  # Replace with your Twilio auth token
    twilio_phone_number = 'your_twilio_phone_number'  # Replace with your Twilio phone number


    client = Client(account_sid ,auth_token )
    message = client.messages.create(
        body = f'Votre code OTP est : {otp}',
        from_=twilio_phone_number,
        to=phone_number
    )
