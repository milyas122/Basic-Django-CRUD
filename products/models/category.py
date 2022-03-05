from django.db import models
import uuid as uuid_lib

class Category(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid_lib.uuid4)
    name = models.CharField(max_length=256)
    isSubCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.name