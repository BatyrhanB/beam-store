from django.contrib import admin

from store.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]
    list_display_links = ("title",)
    search_fields = [
        "title",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["title", "created_at", "updated_at"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price", "created_at", "updated_at"]
    list_display_links = ("title",)
    list_filter = ("category",)
    search_fields = [
        "title",
        "description",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["title", "category", "description", "price", "created_at", "updated_at"]
