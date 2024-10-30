from .permsions import CanCreateProductPremissions, IsOwnerOrReadOnly
from .authentication import TokenAuthentication
from .serializer import ProductSerializer
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes as decorators_permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class CustomThrottle(UserRateThrottle, AnonRateThrottle):
    # def __init__(self, rate='1/day', scope='custom', rate_key='ip', **kwargs):
    #     self.scope = scope
    #     self.rate = rate
    #     self.rate_key = rate_key
    #     super().__init__()
    rate = '5/day'
    scope = 'custom'
    rate_key = 'ip'

# class CustomThrottleMixin: heritance
#     throttle_classes = [CustomThrottle]
#     scope = 'custom'
#     rate = '5/day'
#     rate_key = 'ip'      


class CustomPaginationClass1(LimitOffsetPagination):
    default_limit = 5
    max_limit = 1000



class CustomPaginationClass2(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000



@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@decorators_permission_classes([permissions.AllowAny])
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


class ProductMixinCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        return self.create(request)
    
    

class ProductMixinsApiView(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPaginationClass1
    throttle_classes = [CustomThrottle]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication] # jwt, #basicAuthToken
    permission_classes = [CanCreateProductPremissions]
    
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
    
    
    
    
    