from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Flight
from .forms import BookingForm, JourneyForm


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
    
    if request.method == 'POST':
        # Handle booking form submission
        journey_form = JourneyForm(data=request.POST)
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            journey = journey_form.save(commit=False)
            booking = booking_form.save(commit=False)
            
            # Create a new booking for the user first
            booking.user_id = request.user
            booking.save()
            
            # Now create the journey for this booking
            journey.booking_id = booking.id
            journey.flight_id = flight.id
            journey.save()
            
            # Success message
            messages.add_message(
                request, messages.SUCCESS, 'Flight Booked successfully!'
            )
            
    return render(request, 'booking/flight_detail.html', {
        "flight": flight,
    })