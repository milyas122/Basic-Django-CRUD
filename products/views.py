from math import prod
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import (
    AddProductSerializer, ProductsSerializer
)
from products import serializers

# Create your views here.

@api_view(['GET'])
def productList(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)