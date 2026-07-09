from rest_framework import serializers
from .models import CategoriyModel

class CategoriySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriyModel
        fields = '__all__'
        read_only_fields = ["created_at", "updated_at"]
        
        