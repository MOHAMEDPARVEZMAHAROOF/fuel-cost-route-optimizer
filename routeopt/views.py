from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import RouteOptimization
from .serializers import RouteOptimizationSerializer
import math

@require_http_methods(["GET"])
def health_check(request):
    return JsonResponse({"status": "healthy"})

class RouteOptimizationViewSet(viewsets.ModelViewSet):
    queryset = RouteOptimization.objects.all()
    serializer_class = RouteOptimizationSerializer
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        routes = self.queryset
        total_routes = routes.count()
        total_distance = sum([r.total_distance for r in routes]) if total_routes > 0 else 0
        total_cost = sum([r.total_fuel_cost for r in routes]) if total_routes > 0 else 0
        avg_cost_per_mile = round(total_cost / total_distance, 2) if total_distance > 0 else 0
        
        return Response({"total_routes": total_routes, "total_distance_miles": round(total_distance, 2), "total_fuel_cost": round(total_cost, 2), "average_cost_per_mile": avg_cost_per_mile})


    @action(detail=False, methods=['post'])
    def optimize(self, request):
        serializer = RouteOptimizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)