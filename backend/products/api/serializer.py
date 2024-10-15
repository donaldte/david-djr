from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id']
        
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        return value    
        
        
        
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
    
           