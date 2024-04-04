from rest_framework import generics, permissions, renderers, response
from django_filters import rest_framework as filters

from store.models import Product
from store.serializers.product_serializers import (
    ProductListSerializer,
    ProductCreateSerializer,
    ProductRetrieveUpdateDestroySerializer,
)
from store.filters import ProductFilter


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.filter(is_deleted=False).select_related("category")


class ProductCreateAPIVIew(generics.CreateAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductCreateSerializer
    permission_classes = (permissions.AllowAny,)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductRetrieveUpdateDestroySerializer
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        return self.serializer_class


class ProductListHtmlAPIView(generics.GenericAPIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "product_list.html"

    def get(self, request, *args, **kwargs):
        return response.Response({}, template_name=self.template_name)


class ProductDetailHtmlView(generics.RetrieveAPIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "product_detail.html"

    def get(self, request, *args, **kwargs):
        return response.Response({}, template_name=self.template_name)

class ProductCreateHtmlView(generics.GenericAPIView):
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "product_create.html"

    def get(self, request, *args, **kwargs):
        return response.Response({}, template_name=self.template_name)
