from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  . import views



router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('get-list-commentaires/' , views.getAllCommentaires),
    path('commentaire/<int:pk>/' , views.getCommentaireById),
    path('commentaire/create/' , views.CreateCommentaireView),
    path('commentaire/<int:pk>/update/' , views.updateCommentaireView),
    path('commentaire/<int:pk>/delete/' , views.deleteCommentaireView),
    path('commentaire/<int:pk>/update/partiel/' , views.updatePartialCommentaireView),
]