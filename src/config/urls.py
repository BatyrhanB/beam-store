from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from config.yasg import schema_view

from store.apis.product_apis import ProductListHtmlAPIView, ProductDetailHtmlView, ProductCreateHtmlView


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/", include("user.urls")),
    path("api/v1/", include("store.urls")),
    # html routes
    path("html/product_list/", ProductListHtmlAPIView.as_view(), name="product-list-render"),
    path("html/product_detail/<uuid:pk>/", ProductDetailHtmlView.as_view(), name="product-detail-render"),
    path("html/product_create/", ProductCreateHtmlView.as_view(), name="product-create-html"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
        # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), for debug toolbar
        path(
            settings.DOCS_URL,
            include_docs_urls(
                title="Store API Docs",
                description="API documentation for Store",
            ),
        ),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
