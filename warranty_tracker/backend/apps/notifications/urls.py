
from django.urls import path
from .views import NotificationView
urlpatterns = [
    path('notifications/', NotificationView.as_view()),
    path('notifications/<str:id>/', NotificationView.as_view()),
    path('notifications/<str:id>/read/', NotificationView.as_view()),
]
