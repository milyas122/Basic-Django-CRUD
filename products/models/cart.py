from django.db import models
from . import Product
import uuid as uuid_lib
from . import User 

class Cart(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid_lib.uuid4)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.uuid