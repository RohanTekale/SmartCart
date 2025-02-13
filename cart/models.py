from django.db import models
from products.models import Product
# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    placed_at = models.PositiveIntegerField(default=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"