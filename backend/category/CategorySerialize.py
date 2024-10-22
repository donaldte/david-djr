from rest_framework import serializers
from category.models import Category



class CategorySerializer(serializers.ModelSerializer):
    product_category = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255, read_only=True, source='owner.username')
    description = serializers.CharField(max_length=50)


    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

#ajoute l'utilsateur connecte avant que ca na cree
#on sait que c'est le vendeur ki cree la category
#pour que la category soit relie a un vendeur qui es l'utilisateur connecte car c'est lui ki cre l'objet category
    
    def create(self, validated_data):
        request = self.context.get('request')
        vendeur = request.user
        validated_data['vendeur'] = vendeur
        return super().create(validated_data)
        




    def validate_description(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Description is too short')
        return value    
        