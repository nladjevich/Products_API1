from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quanitity = models.IntegerField()
