from django.urls import path

from store.apis.category_apis import CategoryListAPIView


urlpatterns = [
   path("list/", CategoryListAPIView.as_view(), name="category-list"),
]

