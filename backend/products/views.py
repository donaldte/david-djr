import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_view(request):
    if request.method == 'GET':
        product1 = Product.objects.all().order_by('?').first()
        data = {
            'name': product1.name,
            'description': product1.description,
            'price': product1.price,
        }
        # deserialisation 
        # serialisation
        return JsonResponse(data)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        
        if not name or not description or not price:
            return JsonResponse({'error': 'Invalid request'})
        
        product1 = Product.objects.create(
            name=name,
            description=description,
            price=price
        )
        return JsonResponse({
            'name': product1.name,
            'description': product1.description,
            'price': product1.price,
        })
    
 
    return JsonResponse({'error': 'Invalid request'})