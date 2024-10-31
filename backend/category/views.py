from django.shortcuts import render
from .CategorySerialize import CategorySerializer
from category.models import Category
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from .permissions import MyPermissions , AuthorPermission , IsStaffPermission

@api_view(['GET'])
def getCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategoryById(request , pk):
    category = get_object_or_404(Category , pk)
    serializer = CategorySerializer(category , many=False)
    return Response(serializer.data)


@permission_classes([ permissions.IsAuthenticated , MyPermissions])
@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer( data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
@permission_classes([ permissions.IsAuthenticated , MyPermissions , AuthorPermission])
@api_view(['PUT'])
def updateCategory(request , pk):
    category = get_object_or_404(Category , pk=pk)
    serializer = CategorySerializer(instance = category , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@permission_classes([ permissions.IsAuthenticated , MyPermissions , AuthorPermission])
@api_view(['DELETE'])
def deleteCategory(request , pk): 
    category = get_object_or_404(Category , pk=pk)
    category.delete()
    return Response('Category was deleted')



@api_view(['GET'])
def SearchApiView(request , self):
    queryset = Category.objects.all()
    serialize = CategorySerializer
    qs = super().get_queryset()
    q = self.request.GET.get('q')
    result = Category.objects.none()
    if q is not None:
        user = None
    #si l'utilisateur n'a rien entre 
        if self.request.user.is_authenticated:
            user = self.request.user
    result = qs.search(q , user)
    return result
        
    





