from django.contrib import admin
from django.utils.html import mark_safe

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'image_tag_mini',
    )
    fields = (
        'title',
        'description',
        'price',
        'width',
        'length',
        'on_hold',
        'is_sold',
        'image',
        'image_tag_full',
    )
    readonly_fields = ('image_tag_full',)

    def image_tag_mini(self, product):
        if product.image:
            return mark_safe(f'<img src="{product.image.url}" width="150" height="150" />')
        return "-"
    image_tag_mini.short_description = 'Image'

    def image_tag_full(self, product):
        if product.image:
            return mark_safe(f'<img src="{product.image.url}" />')
        return "-"
    image_tag_full.short_description = 'Full Image'
