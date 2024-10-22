import requests
import random
from django.conf import settings



def send_otp_to_phone(phone_number):
    try:

        otp = random.randint(1 , 3)
        url = f'{otp}'  #aller sur une platforme en ligne de sms/phone_number
        response = requests.get(url)
        return otp

    except Exception as e:
        return None
