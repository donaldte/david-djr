from .serializer import ProductSerializer
from products.models import Product
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@permission_classes([permissions.IsAdminUser , permissions.IsAuthenticated , permissions.IsAuthenticatedOrReadOnly])
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
        
#     elif request.method == "POST":
#         data = request.data
#         serializer = ProductSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             name = serializer.validated_data.get('name')
#             description = serializer.validated_data.get('description')
#             price = serializer.validated_data.get('price')
#             description= name
#             serializer.save(description=description)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
#     elif request.method == "PUT":
#         if pk is not None: 
#             product = get_object_or_404(Product, pk=pk)
#             data = request.data
#             serializer = ProductSerializer(instance=product, data=data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
#         return Response({'error': 'Invalid request enter the pk'}, status=status.HTTP_200_OK)
    
#     elif request.method == "PATCH":
#         if pk is not None: 
#             product = get_object_or_404(Product, pk=pk)
#             data = request.data
#             serializer = ProductSerializer(instance=product, data=data, partial=True)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
#         return Response({'error': 'Invalid request enter the pk'}, status=status.HTTP_200_OK)
    
#     elif request.method == "DELETE":
#         if pk is not None:
#             product = get_object_or_404(Product, pk=pk)
#             product.delete()
#             return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid request enter the pk'}, status=status.HTTP_200_OK)
    
#     return Response({'error': 'Invalid request'}, status=status.HTTP_200_OK)


class ProductMixinsApiView(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication] # jwt, #basicAuthToken
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        return self.list(request)
    
    
    def post(self, request):
        return self.create(request)
    
    
    def put(self, request, pk=None):
        return self.update(request, pk)
    
    
    def patch(self, request, pk=None):
        return self.partial_update(request, pk)
    
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)
    
    
    
#type d'authentification JWT token on utiise le acces token pour acceder aux api
