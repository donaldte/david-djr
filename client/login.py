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

r = requests.post(login_endpoint, data=data)

if r.status_code == 200:
    token = r.json().get('token')
   
    headers = {
        'Authorization': f'Token {token}' #Bearer Token, jwt
    }
    
    r = requests.get(endpoint, headers=headers)
    
    print(r.json())

else:
    print('Invalid credentials')    