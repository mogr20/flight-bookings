from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Flight, Journey, Booking, Passenger
from .forms import PassengerForm


# Create your views here.
class HomePage(generic.ListView):
    """
    Displays the home page.
    Returns all flights in :model:`booking.Flight`
    and displays them in a table.
    **Context**
    
    ``queryset``
        All instances of :model:`booking.Flight`.
    ``template_name``
        html template to send the data to.
    """
    queryset = Flight.objects.all()
    template_name = 'booking/index.html'


def flight_detail(request, flight_id):
    """
    Displays the details of an individual :model:`booking.Flight`.
    Returns the specific flight, if it exists.
    
    **Context**
    
    ``flight``
        The specific :model:`booking.Flight` instance to display.
    ``passenger_form``
        Form to add a new :model:`booking.Passenger`.
    ``queryset``
        All instances of :model:`booking.Flight`.
    ``booking``
        New booking :model:`booking.Booking` instance.
    ``passenger``
        New passenger :model:`booking.Passenger` instance
        for the booking.
    ``journey``
        New Journey :model:`booking.Journey` instance,
        for the booking.
    """
    queryset = Flight.objects.all()
    flight = get_object_or_404(queryset, pk=flight_id)

    if request.method == 'POST':
        # Handles passenger form, and creating a new booking
        passenger_form = PassengerForm(data=request.POST)
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
            messages.add_message(
                request, messages.INFO,
                'You can go to "My Booking" to add more passengers.'
            )
        else:
            print("bookingform.errors", passenger_form.errors)

    passenger_form = PassengerForm()

    return render(request, 'booking/flight_detail.html', {
        "flight": flight,
        "passenger_form": passenger_form,
    })


@login_required
def all_my_bookings(request):
    """
    Displays all of the user's bookings, and flights associated with them.
    Returns all bookings in :model:`booking.Booking` that
    are associated with the user.
    
    **Context**
    ``bookings``
        All instances of :model:`booking.Booking` for the user.
    ``journeys``
        All instances of :model:`booking.Journey` for the
        user's bookings.
    ``flight_list``
        All instances of :model:`booking.Flight` that match
        the user's journeys.
    """
    print("in bookings")
    bookings = Booking.objects.filter(user_id=request.user.id).order_by(
        '-booking_date')

    journeys = Journey.objects.filter(booking_id__in=bookings)
    flight_list = Flight.objects.filter(id__in=journeys.values('flight_id'))

    return render(request, 'booking/my_bookings.html', {
        "booking_list": bookings,
        "journey_list": journeys,
        "flight_list": flight_list,
    })


@login_required
def booking_detail(request, booking_id):
    """
    Displays a specific booking, flight associated with it,
    and passengers associated with it.
    Returns the specific booking, if it exists.
    
    **Context**
    ``booking``
        The specific :model:`booking.Booking` instance to display.
    ``journey``
        The specific :model:`booking.Journey` instance to display,
        linked to the booking.
    ``flight``
        The specific :model:`booking.Flight` instance to display,
        linked to the journey.
    ``passenger_list``
        All instances of :model:`booking.Passenger` that are
        associated with the booking.
    ``passenger_form``
        Form to add a new :model:`booking.Passenger`.
    """
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.user_id.id != request.user.id:
        messages.add_message(
            request, messages.ERROR,
            "You are not authorized to view this booking."
        )
        return HttpResponseRedirect(reverse('my_bookings'))

    journey = get_object_or_404(Journey, booking_id=booking.id)
    flight = get_object_or_404(Flight, pk=journey.flight_id.id)
    passenger_list = Passenger.objects.filter(booking_id=booking.id)

    if request.method == 'POST':
        # Handles passenger form, and creating a new booking
        passenger_form = PassengerForm(data=request.POST)
        if passenger_form.is_valid():
            passenger = passenger_form.save(commit=False)

            # Now add the passengers to the booking
            passenger.booking_id = booking
            passenger.save()

            # Success message
            messages.add_message(
                request, messages.SUCCESS,
                'Passenger added to Booking successfully!'
            )
        else:
            print("bookingform.errors", passenger_form.errors)

    passenger_form = PassengerForm()

    return render(request, 'booking/booking_passengers.html', {
        "booking": booking,
        "journey": journey,
        "flight": flight,
        "passenger_list": passenger_list,
        "passenger_form": passenger_form,
    })


@login_required
def my_journey_delete(request, journey_id):
    """
    Deletes a flight from a booking (by deleting the connecting journey object)
    Returns to the all bookings page for the user, as the booking is deleted.
    
    **Context**
    ``journey``
        The specific :model:`booking.Journey` instance to delete.
    ``booking``
        The specific :model:`booking.Booking` instance to delete,
        which the journey is linked to.
    """
    journey = get_object_or_404(Journey, pk=journey_id)
    booking = get_object_or_404(Booking, pk=journey.booking_id.id)

    if booking.user_id.id != request.user.id:
        messages.add_message(
            request, messages.ERROR,
            "You are not authorized to delete this booking."
        )
        return HttpResponseRedirect(reverse('my_bookings'))

    journey.delete()
    # for now, we delete the booking too,
    # as we only have one flight per booking
    booking.delete()
    messages.add_message(
        request, messages.SUCCESS, "Flight Booking removed."
    )

    return HttpResponseRedirect(reverse('my_bookings'))


@login_required
def edit_passenger(request, booking_id, passenger_id):
    """
    Edits a passenger's details in a booking
    Returns to the booking, with the updated passenger details.
    
    **Context**
    ``passenger``
        The specific :model:`booking.Passenger` instance to edit.
    ``booking``
        The specific :model:`booking.Booking` instance to edit,
        which the passenger is linked
    ``passenger_form``
        Form to edit the :model:`booking.Passenger`.
    """
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    booking = get_object_or_404(Booking, pk=booking_id)
    passenger_form = PassengerForm(data=request.POST, instance=passenger)

    if (booking.user_id.id == request.user.id
            and passenger_form.is_valid()
            and passenger.booking_id.id == booking.id):
        passenger_form.save()
        messages.add_message(
            request, messages.SUCCESS, "Passenger details updated."
        )
    elif passenger_form.is_valid() is False:
        print("passenger_form.errors", passenger_form.errors)
    else:
        messages.add_message(
            request, messages.ERROR,
            "You are not authorized to edit this booking's passenger."
        )

    return HttpResponseRedirect(reverse('booking_detail', args=[booking_id]))


@login_required
def delete_passenger(request, booking_id, passenger_id):
    """
    Deletes a passenger from a booking
    Returns to the booking, with the passenger removed.
    
    **Context**
    ``passenger``
        The specific :model:`booking.Passenger` instance to delete.
    ``booking``
        The specific :model:`booking.Booking` that the
        passenger is linked to.
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
            request, messages.ERROR,
            "You are not authorized to remove this user's passenger."
        )

    return HttpResponseRedirect(reverse('booking_detail', args=[booking_id]))
