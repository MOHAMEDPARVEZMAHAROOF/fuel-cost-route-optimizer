from django.contrib import admin
from .models import RouteOptimization

@admin.register(RouteOptimization)
class RouteOptimizationAdmin(admin.ModelAdmin):
    list_display = ['start_location', 'end_location', 'total_distance', 'total_fuel_cost', 'created_at']
    list_filter = ['created_at']
    search_fields = ['start_location', 'end_location']
    readonly_fields = ['total_fuel_cost', 'gallons_needed', 'created_at', 'updated_at']
