from django.db import models

class Item(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    seasons = models.CharField(max_length=20)
    crops = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='item_photos/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.product_name
