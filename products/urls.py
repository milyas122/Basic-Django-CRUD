from django.urls import path
from . import views 

urlpatterns = [
    path('products/', views.CreateProductView.as_view()),
    path('products/class/', views.ProductCreateDetailUpdateDeleteView.as_view()),
    path('categories/', views.getCategoryList),
    path('subcategories/', views.getSubCategoryList)

]
