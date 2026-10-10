
from django.urls import path
from .views import ServiceCentreList
urlpatterns = [
    path('service-centres/', ServiceCentreList.as_view()),
]
