from rest_framework import generics, permissions

from store.models import Category
from store.serializers.category_serializers import CategoryListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.AllowAny,)
