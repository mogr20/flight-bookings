from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    booking_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    
    
class Passenger(models.Model):
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dietary_requirements = models.TextField()
    baggage_weight = models.FloatField(default=0.0)
    
    
class Airport(models.Model):
    airport_code = models.CharField(max_length=20, unique=True)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=55)
    timezone = models.CharField(max_length=50)
    
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=50)
    scheduled_time = models.DateTimeField()
    flight_num_and_time = models.CharField(max_length=254, unique=True)
    expected_time = models.DateTimeField()
    is_departure = models.BooleanField(default=True)
    status = models.CharField(max_length=50)
    terminal = models.CharField(max_length=20)
    gate = models.CharField(max_length=20)
    arrival_airport = models.ForeignKey(
        Airport, on_delete=models.RESTRICT, default=None, related_name='arrival_airport'
    )
    departure_airport = models.ForeignKey(
        Airport, on_delete=models.RESTRICT, default=None, related_name='departure_airport'
    )
    
    
class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    flight_id = models.ForeignKey(
        Flight, on_delete=models.CASCADE
    )
    is_taken = models.BooleanField(default=False)


class Flight_Seat(models.Model):
    seat_id = models.ForeignKey(
        Seat, on_delete=models.CASCADE
    )
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE
    )
    
    
class Journey(models.Model):
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE
    )
    flight_id = models.ForeignKey(
        Flight, on_delete=models.CASCADE
    )
    layover_duration = models.TimeField(default=None)