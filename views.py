from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from .models import Van, Driver, Route, Schedule

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_vans'] = Van.objects.count()
        context['total_drivers'] = Driver.objects.count()
        context['total_routes'] = Route.objects.count()
        context['total_schedules'] = Schedule.objects.count()
        context['vans_in_maintenance'] = Van.objects.filter(under_maintenance=True).count()
        return context


# --- Van CRUD Views ---
class VanListView(ListView):
    model = Van
    template_name = 'van_list.html'
    context_object_name = 'vans'

class VanCreateView(CreateView):
    model = Van
    template_name = 'van_form.html'
    fields = ['vehicle_number', 'capacity', 'fuel_capacity', 'status', 'under_maintenance']
    success_url = reverse_lazy('van_list')

class VanUpdateView(UpdateView):
    model = Van
    template_name = 'van_form.html'
    fields = ['vehicle_number', 'capacity', 'fuel_capacity', 'status', 'under_maintenance']
    success_url = reverse_lazy('van_list')

class VanDeleteView(DeleteView):
    model = Van
    template_name = 'van_confirm_delete.html'
    success_url = reverse_lazy('van_list')


# --- Driver CRUD Views ---
class DriverListView(ListView):
    model = Driver
    template_name = 'driver_list.html'
    context_object_name = 'drivers'

class DriverCreateView(CreateView):
    model = Driver
    template_name = 'driver_form.html'
    fields = ['name', 'license_number', 'is_available', 'max_working_hours']
    success_url = reverse_lazy('driver_list')

class DriverUpdateView(UpdateView):
    model = Driver
    template_name = 'driver_form.html'
    fields = ['name', 'license_number', 'is_available', 'max_working_hours']
    success_url = reverse_lazy('driver_list')

class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'driver_confirm_delete.html'
    success_url = reverse_lazy('driver_list')


# --- Route CRUD Views ---
class RouteListView(ListView):
    model = Route
    template_name = 'route_list.html'
    context_object_name = 'routes'

class RouteCreateView(CreateView):
    model = Route
    template_name = 'route_form.html'
    fields = ['source', 'destination', 'distance', 'estimated_time', 'passengers', 'priority']
    success_url = reverse_lazy('route_list')

class RouteUpdateView(UpdateView):
    model = Route
    template_name = 'route_form.html'
    fields = ['source', 'destination', 'distance', 'estimated_time', 'passengers', 'priority']
    success_url = reverse_lazy('route_list')

class RouteDeleteView(DeleteView):
    model = Route
    template_name = 'route_confirm_delete.html'
    success_url = reverse_lazy('route_list')


# --- Scheduling Views ---
class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule_list.html'
    context_object_name = 'schedules'

class GenerateSchedulesView(View):
    def post(self, request, *args, **kwargs):
        from .services.csp.solver import CSP, generate_domains, constraint_no_overlap, constraint_working_hours, optimize_domains
        
        # Clear existing schedules (for simplicity in this prototype)
        Schedule.objects.all().delete()
        
        routes = list(Route.objects.all())
        vans = list(Van.objects.all())
        drivers = list(Driver.objects.all())
        
        if not routes or not vans or not drivers:
            messages.error(request, 'Cannot generate schedule: Ensure you have at least one route, one van, and one driver.')
            return HttpResponseRedirect(reverse('schedule_list'))
            
        start_time = timezone.now().replace(hour=8, minute=0, second=0, microsecond=0)
        if start_time < timezone.now():
            start_time += timezone.timedelta(days=1)
            
        # Initialize CSP
        domains = generate_domains(routes, vans, drivers, start_time)
        domains = optimize_domains(domains)
        
        # We need to filter routes that have empty domains
        valid_routes = []
        for r in routes:
            if domains[r]:
                valid_routes.append(r)
            else:
                messages.warning(request, f'No valid assignments found for route: {r}')
                
        if not valid_routes:
            messages.error(request, 'No routes can be fulfilled given the current constraints.')
            return HttpResponseRedirect(reverse('schedule_list'))
            
        constraints = [constraint_no_overlap, constraint_working_hours]
        csp = CSP(variables=valid_routes, domains=domains, constraints=constraints)
        
        # Run Backtracking search
        assignment = csp.backtrack()
        
        if assignment:
            # Save assignments to DB
            for route, val in assignment.items():
                van, driver, t = val
                Schedule.objects.create(
                    route=route,
                    van=van,
                    driver=driver,
                    departure_time=t
                )
            messages.success(request, 'Schedules generated successfully using AI CSP Engine!')
        else:
            messages.error(request, 'Failed to generate a complete schedule satisfying all constraints.')
            
        return HttpResponseRedirect(reverse('schedule_list'))



