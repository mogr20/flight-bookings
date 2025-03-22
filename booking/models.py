from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    """
    
    """
    booking_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.booking_date} - {self.user_id.username}"


class Passenger(models.Model):
    """
    
    """
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dietary_requirements = models.TextField(default="", blank=True)
    baggage_weight = models.CharField(
        default="None",
        blank=True,
        max_length=15,
        choices=[
            ('None', 'None'),
            ('Hand', 'Hand'),
            ('Hold', 'Hold'),
            ('Hand and Hold', 'Hand and Hold')
        ]
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Airport(models.Model):
    """
    
    """
    airport_code = models.CharField(max_length=20, unique=True)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=55)
    timezone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.airport_code} - ({self.city}, {self.airport_name})"


class Flight(models.Model):
    """
    
    """
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=50)
    scheduled_time = models.DateTimeField()
    expected_time = models.DateTimeField(blank=True, null=True)
    arrival_scheduled_time = models.DateTimeField()
    arrival_expected_time = models.DateTimeField(blank=True, null=True)
    is_departure = models.BooleanField(default=True)
    status = models.CharField(max_length=50, blank=True)
    terminal = models.CharField(max_length=20, blank=True)
    gate = models.CharField(max_length=20, blank=True)
    arrival_airport = models.ForeignKey(
        Airport, on_delete=models.SET_NULL, null=True, related_name='arrival_airport'
    )
    departure_airport = models.ForeignKey(
        Airport, on_delete=models.SET_NULL, null=True, related_name='departure_airport'
    )

    def __str__(self):
        return f"{self.flight_num_and_time}"

    @property
    def flight_num_and_time(self):
        return f"{self.flight_number} - {self.scheduled_time}"


class Seat(models.Model):
    """
    
    """
    seat_number = models.CharField(max_length=10)
    flight_id = models.ForeignKey(
        Flight, on_delete=models.CASCADE
    )
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seat_number} - {self.flight_id.flight_num_and_time}"


class Flight_Seat(models.Model):
    """
    
    """
    seat_id = models.ForeignKey(
        Seat, on_delete=models.CASCADE
    )
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.seat_id.seat_number} - {self.booking_id.user_id.username}"


class Journey(models.Model):
    """
    
    """
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE
    )
    flight_id = models.ForeignKey(
        Flight, on_delete=models.CASCADE
    )
    layover_duration = models.TimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.flight_id.flight_number} - {self.booking_id.user_id.username}"
