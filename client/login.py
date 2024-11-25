import requests
from getpass import getpass

endpoint = 'http://localhost:8000/api/v1/products/'
login_endpoint = 'http://localhost:8000/api/v1/login/'
username = input('enter your username:  ')
password = getpass('enter your password:  ')

data = {
    'username': username,
    'password': password
}

product_data = {
    'name': 'New Product new',
    'description': 'New Product Description',
    'price': 100
}

r = requests.post(login_endpoint, data=data)

if r.status_code == 200:
    token = r.json().get('token')
    print(token)
   
    headers = {
        'Authorization': f'Bearer {token}' #Bearer Token, jwt
    }
    
    r = requests.post(endpoint, headers=headers, json=product_data)
    
    print(r.json())

else:
    r= requests.post(endpoint, json=product_data)
    
    print(r.json())    