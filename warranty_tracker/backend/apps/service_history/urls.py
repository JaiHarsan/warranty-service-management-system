
from django.urls import path
from .views import ServiceHistoryView
urlpatterns = [
    path('products/<str:product_id>/service-history/', ServiceHistoryView.as_view()),
]
