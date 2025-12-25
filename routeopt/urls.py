from django.urls import path
from .views import health_check, RouteOptimizationViewSet

urlpatterns = [
    path('health/', health_check),
]
