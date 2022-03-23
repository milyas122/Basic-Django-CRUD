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
from . mixins import (
    StaffEditorPermissionMixin
)
from products import serializers
from .permissions import (
    isStaffEditorPermission
)
from rest_framework import mixins, permissions, authentication
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

class ProductCreateDetailUpdateDeleteView(StaffEditorPermissionMixin,APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [isStaffEditorPermission]
    authentication = [authentication.SessionAuthentication]
    

    def get(self,request, pk=None, format=None): 
        serializers = ListProductsSerializer(self.get_queryset(pk), many=True)
        return Response(serializers.data)
    
    def post(self,request, format=None):
        serializer = AddProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_queryset(self,pk):
        if pk:
            return Product.objects.filter(uuid=pk).defer("slug","created_at","updated_at")
        else: 
            return Product.objects.defer("slug","created_at","updated_at")

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