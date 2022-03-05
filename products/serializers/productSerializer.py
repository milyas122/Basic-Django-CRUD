from rest_framework import serializers
from ..models import Product

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "quantity", "price", "description", "image_url", "category", "sub_category"]

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"