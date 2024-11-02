# test_models.py
import pytest

from products.models import Product



@pytest.mark.django_db
def test_product_name(product):
    assert product.get_product_name() == 'testproduct'
    
@pytest.mark.django_db
def test_product_description(product):
    assert product.get_product_description() == 'testdescription'
    
    
@pytest.mark.django_db
def test_product_price(product):
    assert product.get_product_price() == 100
    
@pytest.mark.django_db
def test_product_owner(product):
    assert product.get_product_owner().username == 'testuser'        