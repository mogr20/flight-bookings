from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Flight, Journey
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
    print("this is request:",request.method)

    if request.method == 'POST':
        print("in request.post")
        # Handle booking form submission
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            print("in validation")
            booking = booking_form.save(commit=False)

            # Create a new booking for the user first
            booking.user_id = request.user
            booking.save()
            print("created booking", booking)

            # Now create the journey for this booking
            Journey.objects.create(booking_id=booking, flight_id=flight)

            # Success message
            messages.add_message(
                request, messages.SUCCESS, 'Flight Booked successfully!'
            )
        else:
            print("bookingform.errors", booking_form.errors)

    journey_form = JourneyForm()
    booking_form = BookingForm()

    return render(request, 'booking/flight_detail.html', {
        "flight": flight,
    })
