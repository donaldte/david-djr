import pytest
import logging 
from django.urls import reverse


logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_product_create(api_client, user):
    url = '/api/v1/products_1/'
    data = {
        'name': 'testproduct',
        'description': 'testdescription',
        'price': 100
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['name'] == 'testproduct'
    assert response.data['description'] == 'testproduct'
    assert response.data['price'] == 100
    assert response.data['owner'] == user.id
    logger.info(response.data)
    
    
# @pytest.mark.django_db
# def test_product_create_with_authentication(api_client, user):
#     url = reverse('api_products')
#     data = {
#         'name': 'testproduct',
#         'description': 'testdescription',
#         'price': 100
#     }
#     api_client.force_authenticate(user=user)
#     response = api_client.post(url, data, format='json')
#     assert response.status_code == 201
#     assert response.data['name'] == 'testproduct'
#     assert response.data['description'] == 'testdescription'
#     assert response.data['price'] == 100
#     logger.info(response.data)