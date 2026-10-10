
from django.urls import path
from .views import ProductList, ProductDetail, ProductUpload
urlpatterns = [
    path('products/upload/', ProductUpload.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<str:id>/', ProductDetail.as_view()),
]
