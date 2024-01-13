from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="$ (CAD)")
    width = models.DecimalField(max_digits=10, decimal_places=1, help_text='inches')
    length = models.DecimalField(max_digits=10, decimal_places=1, help_text='inches')
    image = models.ImageField(upload_to='product_images/')
    on_hold = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
