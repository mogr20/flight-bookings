from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Flight, Journey, Booking, Passenger
from .forms import NewBookingPassengerForm

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
        # Handles passenger form, and creating a new booking
        passenger_form = NewBookingPassengerForm(data=request.POST)
        if passenger_form.is_valid():
            passenger = passenger_form.save(commit=False)

            # Create a new booking for the user first
            booking = Booking.objects.create(user_id=request.user)

            # Now add the passengers to the booking
            passenger.booking_id = booking
            passenger.save()

            # Now create the journey for this booking
            Journey.objects.create(booking_id=booking, flight_id=flight)

            # Success message
            messages.add_message(
                request, messages.SUCCESS, 'Flight Booked successfully!'
            )
        else:
            print("bookingform.errors", passenger_form.errors)

    passenger_form = NewBookingPassengerForm()

    return render(request, 'booking/flight_detail.html', {
        "flight": flight,
        "passenger_form": passenger_form,
    })

@login_required
def all_my_bookings(request, user_id):
    """
    Displays all of the user's bookings, and flights associated with them.
    """
    bookings = Booking.objects.filter(user_id=user_id).order_by('-booking_date')

    journeys = Journey.objects.filter(booking_id__in=bookings)
    flight_list = Flight.objects.filter(id__in=journeys.values('flight_id'))

    return render(request, 'booking/my_bookings.html', {
        "booking_list": bookings,
        "journey_list": journeys,
        "flight_list": flight_list,
        "username": user_id,
    })

@login_required
def booking_detail(request, user_id, booking_id):
    """
    Displays a specific booking, flights associated with it, and customers associated with it.
    """
    booking = Booking.objects.get(user_id=request.user.id, id=booking_id)

    journey = Journey.objects.get(booking_id=booking.id)
    flight = Flight.objects.get(id=journey.flight_id.id)
    passenger_list = Passenger.objects.filter(booking_id=booking.id)

    if request.method == 'POST':
        # Handles passenger form, and creating a new booking
        passenger_form = NewBookingPassengerForm(data=request.POST)
        if passenger_form.is_valid():
            passenger = passenger_form.save(commit=False)

            # Now add the passengers to the booking
            passenger.booking_id = booking
            passenger.save()

            # Success message
            messages.add_message(
                request, messages.SUCCESS, 'Flight Booked successfully!'
            )
        else:
            print("bookingform.errors", passenger_form.errors)

    passenger_form = NewBookingPassengerForm()

    return render(request, 'booking/booking_passengers.html', {
        "booking": booking,
        "journey": journey,
        "flight": flight,
        "passenger_list": passenger_list,
        "passenger_form": passenger_form,
        "username": user_id,
    })

@login_required
def my_journey_delete(request, user_id, journey_id):
    """
    Deletes a flight from a booking (by deleting the connecting journey object)
    """
    journey = get_object_or_404(Journey, pk=journey_id)
    booking = get_object_or_404(Booking, pk=journey.booking_id.id)

    if booking.user_id.id == request.user.id:
        journey.delete()
        # for now, we delete the booking too, as we only have one flight per booking
        booking.delete()
        messages.add_message(
            request, messages.SUCCESS, "Flight Booking removed."
        )
    else:
        messages.add_message(
            request, messages.ERROR, "You are not authorized to remove this user's booked flight."
        )

    return HttpResponseRedirect(reverse('my_bookings', args=(request.user.id,)))

@login_required
def edit_passenger(request, user_id, booking_id, passenger_id):
    """
    Edits a passenger's details in a booking
    """
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    booking = get_object_or_404(Booking, pk=booking_id)
    passenger_form = NewBookingPassengerForm(data=request.POST, instance=passenger)

    if booking.user_id.id == request.user.id and passenger_form.is_valid():
        passenger_form.save()
        messages.add_message(
            request, messages.SUCCESS, "Passenger details updated."
        )
    elif passenger_form.is_valid() is False:
        print("passenger_form.errors", passenger_form.errors)
    else:
        messages.add_message(
            request, messages.ERROR, "You are not authorized to edit this booking's passenger."
        )

    return HttpResponseRedirect(reverse('booking_detail', args=(request.user.id, booking_id)))

@login_required
def delete_passenger(request, user_id, booking_id, passenger_id):
    """
    Deletes a passenger from a booking
    """
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    booking = get_object_or_404(Booking, pk=booking_id)

    if booking.user_id.id == request.user.id:
        passenger.delete()
        messages.add_message(
            request, messages.SUCCESS, "Passenger removed from booking."
        )
    else:
        messages.add_message(
            request, messages.ERROR, "You are not authorized to remove this user's passenger."
        )

    return HttpResponseRedirect(reverse('booking_detail', args=(request.user.id, booking_id)))
