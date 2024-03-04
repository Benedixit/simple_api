from rest_framework import serializers
from .models import Product, Reviews
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

class UserTokenSerializer(serializers.Serializer):
    user = UserSerializer()
    token = TokenSerializer()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'product_detail', 'specifications', 'category', 'seller']


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'review_text', 'product']
