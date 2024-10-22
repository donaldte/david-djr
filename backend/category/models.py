from django.db import models
from products.models import Product
from django.db.models import Q



class CategoryQuerySet(models.QuerySet):
    def is_public(self):
          return self.filter(public=True)
     

    def get_queryset(self):
        return CategoryQuerySet(self.model , using=self.db)

    def search(self , query , user=None):
          lookup = Q(name__contains=query) | Q(description__contains=query)
          qs = self.filter(lookup)
          #si le user n'xiste pas on le renoit ses categori
          if user is not None:
               qs2 = self.filter(user=user).filter(lookup)
               qs = (qs | qs2).distinct()
          return qs
     

     
class CategoryManager(models.Manager):
    def search(self , query , user=None):
         return self.get_queryset().is_public().search(query, user)
      


class Category(models.Model):
        product_category = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
        name = models.CharField(max_length=100)
        description = models.CharField(max_length=50)
        vendeur = models.ForeignKey("auth.User"  , null=True , blank=True , on_delete=models.CASCADE)
        public = models.BooleanField(default=False)

        objects = CategoryManager()

        def __str__(self):
            return self.product_category.name + "---" + self.name
