from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class RouteOptimization(models.Model):
    start_location = models.CharField(max_length=255)
    start_lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    start_lon = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    
    end_location = models.CharField(max_length=255)
    end_lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    end_lon = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    
    total_distance = models.FloatField()
    route_data = models.JSONField(default=dict)
    
    vehicle_mpg = models.FloatField(default=10, validators=[MinValueValidator(1)])
    fuel_price_per_gallon = models.FloatField(default=3.50, validators=[MinValueValidator(0)])
    total_fuel_cost = models.FloatField()
    gallons_needed = models.FloatField()
    
    fuel_stops = models.JSONField(default=list)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.start_location} to {self.end_location}"
    
    def save(self, *args, **kwargs):
        self.gallons_needed = round(self.total_distance / self.vehicle_mpg, 2)
        self.total_fuel_cost = round(self.gallons_needed * self.fuel_price_per_gallon, 2)
        super().save(*args, **kwargs)
