from django.db import models
from . import Product
import uuid as uuid_lib
from . import User 

class Cart(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid_lib.uuid4)
    quantity = models.IntegerField(default=0)
    amount = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "cart"
        
    def __str__(self):
        return self.uuid