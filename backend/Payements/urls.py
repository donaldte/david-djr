from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  . import views



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    # path('get-list-payements/' , views.getAllCommentaires),
    # path('payements/<int:pk>/' , views.getCommentaireById),
    # path('payements/create/' , views.CreateCommentaireView),
    # path('payements/<int:pk>/update/' , views.updateCommentaireView),
    # path('payements/<int:pk>/delete/' , views.deleteCommentaireView),
    # path('payements/<int:pk>/update/partiel/' , views.updatePartialCommentaireView),
]