from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models. IntegerField()
    published_on = models.DateField()

    # decorator
    # This function returns a boolean if we still have some products inside of a stock
    @property
    def is_in_stock(self):
        return self.quantity > 0
