import pytest
import logging 
from django.urls import reverse


logger = logging.getLogger(__name__)


#test creation sans etre authentifie au preable
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
    
    


#test creation avec authentification au preable
@pytest.mark.django_db
def test_product_create_with_authentication(api_client, user):
    url = reverse('api_products')
    data = {
        'name': 'testproduct',
        'description': 'testdescription',
        'price': 100
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['name'] == 'testproduct'
    assert response.data['description'] == 'testdescription'
    assert response.data['price'] == 100
    logger.info(response.data)




@pytest.mark.django_db
def test_product_get(api_client , user):
    url = '/api/v1/products_1/'


    data = {
        'name': 'testproduct',
        'description': 'testdescription',
        'price': 100
    }

    test_product_create(api_client ,user)
    # response = api_client.post(url, data, format='json')

    reponse = api_client.get(url , format='json')
    assert reponse.status_code == 200
    assert len (reponse.data) == 1




@pytest.mark.django_db
def test_product_update(api_client , product , user ):
    url = f'/api/v1/products/{product.pk}/'

    data = {
         'name': 'producttest',
        'description': 'descriptiontest',
        'price': 200
    }

    api_client.force_authenticate(user=user)

    response = api_client.put(url , data , format='json')
    assert response.status_code == 200
    assert response.data['name'] == 'producttest'
    assert response.data['description'] == 'descriptiontest'
    assert response.data['price'] == 200
    logger.info(response.data)







@pytest.mark.django_db
def test_product_delete(api_client ,  product , user):
    url = f'/api/v1/products/{product.pk}/'

    api_client.force_authenticate(user=user)
    response = api_client.delete(url , format='json')
   
    assert response.status_code == 204
    response2 = api_client.get(url ,format='json')
    assert response2.status_code == 404
    logger.info(response.data)




