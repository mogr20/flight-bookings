from django import forms
from .models import Passenger, Journey


class PassengerForm(forms.ModelForm):
    """
    Form class for a user to add a passenger to an existing booking
    """
    class Meta:
        model = Passenger
        fields = ('first_name', 'last_name', 'dietary_requirements',
                  'baggage_weight',)


class JourneyForm(forms.ModelForm):
    """
    Form class for a user to add a flight to their journey,
    which is linked to their booking
    """
    class Meta:
        model = Journey
        fields = ('booking_id', 'flight_id', 'layover_duration',)
