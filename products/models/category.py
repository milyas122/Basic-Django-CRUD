from django.db import models
import uuid as uuid_lib

class SubCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isSubCategory=True)

class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isSubCategory=False)

class Category(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid_lib.uuid4)
    name = models.CharField(max_length=256, unique=True)
    isSubCategory = models.BooleanField(default=False)

    # Model managers
    objects = models.Manager()  # The default manager.
    category_object = CategoryManager()  # Our custom manager.
    subcategory_object = SubCategoryManager()  # Our custom manager.
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}({self.uuid})"