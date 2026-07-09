from django.contrib.auth import get_user_model,authenticate
from rest_framework import serializers
from .models import UserModel

User=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=["id","username",'password']
        
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        user=authenticate(
            username=attrs["username"],
            password=attrs["password"]
        )
        if not user:
            raise serializers.ValidationError("username yoki parol xato")
        attrs["user"] = user
        return attrs
    
class UserRoleChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=["id","role"]
        
class UserViewserializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=["id","username","role"]