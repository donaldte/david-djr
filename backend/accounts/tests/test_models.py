# test_models.py
import pytest

from accounts.models import CustomUser



@pytest.mark.django_db
def test_account_email(CustomerUser):
    assert CustomerUser.get_user_email() == 'paulnicolas519@gmail.com'
    
@pytest.mark.django_db
def test_account_otp(CustomerUser):
    assert CustomerUser.get_account_otp() == '2345'
    

@pytest.mark.django_db
def test_account_password(CustomerUser):
    assert CustomerUser.get_account_password() == '12345'
    