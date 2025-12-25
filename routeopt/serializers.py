from rest_framework import serializers
from .models import RouteOptimization

class RouteOptimizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteOptimization
        fields = ['id', 'start_location', 'start_lat', 'start_lon', 'end_location', 'end_lat', 'end_lon', 'total_distance', 'vehicle_mpg', 'fuel_price_per_gallon', 'total_fuel_cost', 'gallons_needed', 'fuel_stops', 'route_data', 'created_at']
        read_only_fields = ['id', 'total_fuel_cost', 'gallons_needed', 'created_at']
