from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from routeopt.views import RouteOptimizationViewSet, health_check

router = routers.SimpleRouter()
router.register(r'optimize', RouteOptimizationViewSet, basename='optimize')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/health/', health_check),
    path('api/v1/', include(router.urls)),
]
