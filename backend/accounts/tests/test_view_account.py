import pytest
import logging 
from django.urls import reverse


logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_account_register(api_client):
    url = reverse('register')

    data = {
        'email':'paulnicolas519@gmail.com',
        'password':'1234',
        'username':'david',
        'password2':'1234'
    }

    response = api_client.post(url , data , format='json')

    assert response.status_code == 201
    assert response.data['email'] == 'paulnicolas519@gmail.com'
    assert response.data['password'] == '1234'
    assert response.data['username'] == 'david'
    assert response.data['password2'] == '1234'
    logger.info(response.data)


@pytest.mark.django_db
def test_account_login(api_client):
    url = reverse('login-with-otp')

    data = {
        'email':'paulnicolas519@gmail.com',
        'password':'1234',
    }

    response = api_client.post(url , data , format='json')

    assert response.status_code == 201
    assert response.data['email'] == 'paulnicolas519@gmail.com'
    assert response.data['password'] == '1234'
    logger.info(response.data)




@pytest.mark.django_db
def test_account_change_password(api_client):
    url = reverse('change-password')

    data = {
        'old_password':'paulnicolas519@gmail.com',
        'new_password':'1234',
    }

    response = api_client.post(url , data , format='json')

    assert response.status_code == 201
    assert response.data['old_password'] == 'paulnicolas519@gmail.com'
    assert response.data['new_password'] == '1234'

    logger.info(response.data)