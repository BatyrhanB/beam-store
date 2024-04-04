from django.urls import path, include


urlpatterns = [
    path("product/", include("store.routes.product_routes"), name="product-main"),
    path("category/", include("store.routes.category_routes"), name="category-main"),
]
