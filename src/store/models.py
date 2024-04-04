from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Title"))

    def __str__(self):
        return f"Category: {self.title}"

    class Meta:
        db_table = "store__categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(BaseModel):
    category = models.ForeignKey(
        "store.Category",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="prodcuts",
        verbose_name=_("Category"),
    )
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("Title"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name=_("Price"))

    def __str__(self):
        return f"Product: {self.title}"

    class Meta:
        db_table = "store__products"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
