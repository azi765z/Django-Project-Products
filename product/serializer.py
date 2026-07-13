from rest_framework import serializers
from .models import ProductModel

class ProductsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="sub_category.category.name",read_only=True)
    sub_category_name = serializers.CharField(source="sub_category.name",read_only=True)

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "name",
            "description",
            "author",
            "sub_category",
            "sub_category_name",
            "category_name",
            "price",
            "stock",
            'image',
            "created_at",
        ]

        read_only_fields = [
            "id",
            "author",
            "created_at"
        ]
    