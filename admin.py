from django.contrib import admin
from .models import Van, Driver, Route, Schedule

@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'capacity', 'fuel_capacity', 'status', 'under_maintenance')
    list_filter = ('status', 'under_maintenance')
    search_fields = ('vehicle_number',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'is_available', 'max_working_hours')
    list_filter = ('is_available',)
    search_fields = ('name', 'license_number')


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination', 'distance', 'estimated_time', 'passengers', 'priority')
    list_filter = ('priority',)
    search_fields = ('source', 'destination')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('route', 'van', 'driver', 'departure_time')
    list_filter = ('departure_time',)
    search_fields = ('route__source', 'route__destination', 'van__vehicle_number', 'driver__name')
