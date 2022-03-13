from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import (
    Product, Category
)
from .serializers import (
    ProductsSerializer,
    CategorySerializer,
    ListProductsSerializer,
    AddProductsSerializer
)
from products import serializers

from rest_framework import mixins
from rest_framework.generics import GenericAPIView

# Create your views here.

class ForceCRSFAPIView(GenericAPIView):
    @classmethod
    def as_view(cls, **initkwargs):
        # Force enables CSRF protection.  This is needed for unauthenticated API endpoints
        # because DjangoRestFramework relies on SessionAuthentication for CSRF validation
        view = super().as_view(**initkwargs)
        view.csrf_exempt = False
        return view

class ProductCreateDetailUpdateDeleteView(APIView):

    def get(self,request,format=None):
        products = Product.objects.defer("slug","created_at","updated_at")
        serializers = ListProductsSerializer(products,many=True)
        return Response(serializers.data)
    
    def post(self,request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            # category = serializer.get("category")
            # sub_category = serializer.get("sub_category")
            # serializer.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CreateProductView(mixins.CreateModelMixin, ForceCRSFAPIView):
    serializer_class = AddProductsSerializer

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(['GET'])
def productList(request):
    if request.method == 'GET':
        products = Product.objects.defer("slug","created_at","updated_at")
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

# @api_view(['POST'])
# def addProductView(request):
#     if request.method == 'POST':
#         pass

@api_view(['GET'])
def getCategoryList(request):
    if request.method == "GET":
        categories = Category.category_object.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def getSubCategoryList(request):
    if request.method == "GET":
        categories = Category.subcategory_object.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)