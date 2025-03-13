from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Flight, Journey, Booking
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
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)

            # Create a new booking for the user first
            booking.user_id = request.user
            booking.save()

            # Now create the journey for this booking
            Journey.objects.create(booking_id=booking, flight_id=flight)

            # Success message
            messages.add_message(
                request, messages.SUCCESS, 'Flight Booked successfully!'
            )
        else:
            print("bookingform.errors", booking_form.errors)

    booking_form = BookingForm()

    return render(request, 'booking/flight_detail.html', {
        "flight": flight,
    })

def my_booking(request, user_id):
    """
    Displays all of the user's bookings
    """
    print("request.user: ", request.user)
    bookings = Booking.objects.filter(user_id=user_id)
    print("booking: ", bookings)

    journeys = Journey.objects.filter(booking_id__in=bookings)
    flight_list = Flight.objects.filter(id__in=journeys)
    print("flight_list: ", flight_list)

    return render(request, 'booking/my_booking.html', {
        "booking_list": bookings,
        "journey_list": journeys,
        "flight_list": flight_list,
        "username": user_id,
    })
