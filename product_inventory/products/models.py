from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    distributor_price = models.CharField(max_length=255)

    def __str__(self):
        return self.name
