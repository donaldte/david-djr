import pytest 
from django.contrib.auth.models import User
from products.models import Product
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    yield APIClient()


@pytest.fixture
def user() -> User:
    return User.objects.create_user(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)


@pytest.fixture
def product(user) -> Product:
    return Product.objects.create(name='testproduct', description='testdescription', price=100, owner=user)