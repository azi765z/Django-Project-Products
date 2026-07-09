from rest_framework import serializers
from .models import ProductModel

class ProductsSerializer(serializers.ModelSerializer):
    categories_name = serializers.CharField(source='categories.categories.name', read_only=True)
    sub_categories_name = serializers.CharField(source='sub_categories.name', read_only=True)
    
    class Meta:
        model = ProductModel
        fields = ["id", "name", "description", "price", "stock", "categories_name", "sub_categories_name", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
        
        
        def create(self, validated_data):
            sub_categories = validated_data.get('sub_categories')
            validated_data['categories'] = sub_categories.categories
            return ProductModel.objects.create(**validated_data)
        