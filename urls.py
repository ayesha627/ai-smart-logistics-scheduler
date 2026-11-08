from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Vans
    path('vans/', views.VanListView.as_view(), name='van_list'),
    path('vans/add/', views.VanCreateView.as_view(), name='van_create'),
    path('vans/<int:pk>/edit/', views.VanUpdateView.as_view(), name='van_update'),
    path('vans/<int:pk>/delete/', views.VanDeleteView.as_view(), name='van_delete'),

    # Drivers
    path('drivers/', views.DriverListView.as_view(), name='driver_list'),
    path('drivers/add/', views.DriverCreateView.as_view(), name='driver_create'),
    path('drivers/<int:pk>/edit/', views.DriverUpdateView.as_view(), name='driver_update'),
    path('drivers/<int:pk>/delete/', views.DriverDeleteView.as_view(), name='driver_delete'),

    # Routes
    path('routes/', views.RouteListView.as_view(), name='route_list'),
    path('routes/add/', views.RouteCreateView.as_view(), name='route_create'),
    path('routes/<int:pk>/edit/', views.RouteUpdateView.as_view(), name='route_update'),
    path('routes/<int:pk>/delete/', views.RouteDeleteView.as_view(), name='route_delete'),

    # Schedules
    path('schedules/', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/generate/', views.GenerateSchedulesView.as_view(), name='schedule_generate'),
]
