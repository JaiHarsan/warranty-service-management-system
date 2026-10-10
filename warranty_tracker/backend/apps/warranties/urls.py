
from django.urls import path
from .views import WarrantyList
urlpatterns = [
    path('warranties/', WarrantyList.as_view()),
]
