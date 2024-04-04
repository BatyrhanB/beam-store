from rest_framework import serializers

from store.models import Product
from store.serializers.category_serializers import CategoryListSerializer

class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = Product
        fields = ["id", "title", "category", "description", "price", "created_at"]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "category", "description", "price", "created_at"]
        read_only_fields = ["id", "created_at"]


class ProductRetrieveUpdateDestroySerializer(ProductCreateSerializer):
    pass
