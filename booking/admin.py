from django.contrib import admin
from .models import Booking, Passenger, Airport, Flight, Seat, Journey


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'booking_date')
    search_fields = ('id', 'user_id',)
    list_filter = ('user_id',)
    ordering = ('-booking_date',)


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'booking_id', 'baggage_weight')
    search_fields = ('first_name', 'last_name', 'booking_id',)
    list_filter = ('booking_id', 'baggage_weight',)
    ordering = ('last_name',)


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('airport_code', 'airport_name', 'city', 'country')
    search_fields = ('airport_code', 'airport_name', 'city', 'country')
    list_filter = ('country',)
    ordering = ('airport_code',)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'airline', 'scheduled_time',
                    'expected_time', 'departure_airport',
                    'arrival_scheduled_time', 'arrival_expected_time',
                    'arrival_airport', 'status', 'terminal', 'gate')
    search_fields = ('flight_number', 'airline', 'scheduled_time',
                     'expected_time', 'departure_airport',
                     'arrival_scheduled_time', 'arrival_expected_time',
                     'arrival_airport', 'status', 'terminal', 'gate',)
    list_filter = ('flight_number', 'airline', 'status', 'terminal',
                   'gate', 'arrival_airport', 'departure_airport')

    def save_model(self, request, obj, form, change):
        if not obj.expected_time:
            obj.expected_time = obj.scheduled_time
        if not obj.arrival_expected_time:
            obj.arrival_expected_time = obj.arrival_scheduled_time
        super().save_model(request, obj, form, change)
    ordering = ('scheduled_time',)


admin.site.register(Seat)


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_id', 'flight_id',)
    search_fields = ('booking_id', 'flight_id',)
    list_filter = ('booking_id', 'flight_id',)
    ordering = ('-booking_id',)
