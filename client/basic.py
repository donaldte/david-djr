import requests


endpoint = 'http://localhost:8000/api/v1/products/1/'
product_data = {'price': 24.90}

response = requests.get(endpoint, json=product_data)
# params 
# session authentication 

# -> entre username et le password --> session id. selenium 

# headers

print(response.json())

print(response.status_code)