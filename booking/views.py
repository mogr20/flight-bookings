from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import Flight


# Create your views here.
class HomePage(generic.ListView):
    """
    Displays the home page.
    """
    queryset = Flight.objects.all()
    template_name = 'booking/index.html'
    
    
def flight_detail(request, flight_id):
    """
    Displays the details of an individual :model:`booking.Flight`.
    """
    queryset = Flight.objects.all()
    flight = get_object_or_404(queryset, pk=flight_id)
    
    return render(request, 'booking/flight_detail.html', {
        "flight": flight,
    })