
from django.urls import path
from .views import HealthCheckView, HealthReportView
urlpatterns = [
    path('health-check/', HealthCheckView.as_view()),
    path('health-checks/<str:id>/', HealthReportView.as_view()),
]
