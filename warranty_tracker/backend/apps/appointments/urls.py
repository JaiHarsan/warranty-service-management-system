
from django.urls import path
from .views import AppointmentView
urlpatterns = [
    path('appointments/', AppointmentView.as_view()),
]
