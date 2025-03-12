from django import forms
from .models import Booking, Passenger, Journey


class BookingForm(forms.ModelForm):
    """
    Form class for a user to make a booking for their journey
    """
    class Meta:
        model = Booking
        fields = ('user_id',)
        
        
class PassengerForm(forms.ModelForm):
    """
    Form class for a user to add a passenger to a booking
    """
    class Meta:
        model = Passenger
        fields = ('booking_id', 'first_name', 'last_name', 'dietary_requirements', 'baggage_weight',)
        
        
class JourneyForm(forms.ModelForm):
    """
    Form class for a user to add a flight to their journey, which is linked to their booking
    """
    class Meta:
        model = Journey
        fields = ('booking_id', 'flight_id', 'layover_duration',)