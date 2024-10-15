from .serializer import ProductSerializer
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin



@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def api_view_products(request, pk=None, *args, **kwargs):
    
    if request.method == "GET":
        if pk:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name')
            description = serializer.validated_data.get('description')
            price = serializer.validated_data.get('price')
            description= name
            serializer.save(description=description)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    elif request.method == "PUT":
        if pk is not None: 
            product = get_object_or_404(Product, pk=pk)
            data = request.data
            serializer = ProductSerializer(instance=product, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        return Response({'error': 'Invalid request enter the pk'}, status=status.HTTP_200_OK)
    
    elif request.method == "PATCH":
        if pk is not None: 
            product = get_object_or_404(Product, pk=pk)
            data = request.data
            serializer = ProductSerializer(instance=product, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        return Response({'error': 'Invalid request enter the pk'}, status=status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid request enter the pk'}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid request'}, status=status.HTTP_200_OK)
    