from rest_framework import serializers
from ..models import Product, Category


class CategoryNameField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.name}"

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ["created_at","updated_at"]
    
    # def create(self, validated_data):
    #     print(validated_data)
    #     category = validated_data.pop('category')
    #     sub_category = validated_data.pop('sub_category')
        
    #     category_obj, created = Category.objects.get_or_create(**category)
    #     subcategory_obj, created = Category.objects.get_or_create(**sub_category)
    #     product = Product.objects.create(category=category_obj,sub_category=subcategory_obj, **validated_data)
    #     return product

class AddProductsSerializer(ProductsSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.category_object.all())
    sub_category = serializers.PrimaryKeyRelatedField(queryset=Category.subcategory_object.all(), required = False)
    
    # class Meta:
    #     model = Product
    #     fields = ["title", "quantity", "price", "description", "image_url", "category", "sub_category"]
    
class ListProductsSerializer(ProductsSerializer):
    category = CategoryNameField(read_only=True)
    sub_category = CategoryNameField(read_only=True)


