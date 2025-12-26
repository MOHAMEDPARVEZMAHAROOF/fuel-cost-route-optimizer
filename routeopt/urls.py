from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import health_check, RouteOptimizationViewSet

urlpatterns = [
    path('health/', health_check),
]

router = DefaultRouter()
router.register(r'optimize', RouteOptimizationViewSet, basename='route-optimize')


urlpatterns += router.urls