from rest_framework import serializers
from .models import SubCategoryModel

class SubCategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.StringRelatedField()  
    class Meta:
        model = SubCategoryModel
        fields = '__all__'
        read_only_fields = ["created_at", "updated_at"]