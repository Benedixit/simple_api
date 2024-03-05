from rest_framework import serializers
from .models import Product, Reviews



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'product_detail', 'specifications', 'category', 'seller']


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'review_text', 'product']
