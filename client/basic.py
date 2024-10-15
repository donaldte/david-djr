import requests


endpoint = 'http://localhost:8000/api/v1/products/4/'
product_data = {'price': 24.90}

response = requests.delete(endpoint, json=product_data)
# params 

# headers

print(response.json())

print(response.status_code)