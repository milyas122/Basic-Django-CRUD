import uuid as uuid_lib
from django.db import models
from . import Category
from django.utils.text import slugify



class Product(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField()
    rating = models.FloatField(blank=True)
    description = models.TextField()
    image_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, related_name='category',on_delete=models.RESTRICT)
    sub_category = models.ForeignKey(Category, related_name='sub_category',on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.uuid}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
