from django.contrib import admin
from .models import Booking, Passenger, Airport, Flight, Seat, Journey

# Register your models here.
admin.site.register(Booking)
admin.site.register(Passenger)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Journey)