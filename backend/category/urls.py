from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  . import views



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('get-list/' , views.getCategory),
    path('category/<int:pk>/' , views.getCategoryById),
    path('category/create/' , views.createCategory),
    path('category/<int:pk>/update/' , views.updateCategory),
    path('category/<int:pk>/delete/' , views.deleteCategory),
    path('api/category/search/' , views.SearchApiView),
]