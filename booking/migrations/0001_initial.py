# Generated by Django 4.2.20 on 2025-03-11 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_code', models.CharField(max_length=20, unique=True)),
                ('airport_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=55)),
                ('timezone', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('airline', models.CharField(max_length=50)),
                ('scheduled_time', models.DateTimeField()),
                ('expected_time', models.DateTimeField(blank=True, null=True)),
                ('is_departure', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('terminal', models.CharField(blank=True, max_length=20)),
                ('gate', models.CharField(blank=True, max_length=20)),
                ('arrival_airport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrival_airport', to='booking.airport')),
                ('departure_airport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departure_airport', to='booking.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('is_taken', models.BooleanField(default=False)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dietary_requirements', models.TextField(blank=True, default='')),
                ('baggage_weight', models.FloatField(default=0.0, null=True)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layover_duration', models.TimeField(blank=True, default=None, null=True)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Flight_Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.seat')),
            ],
        ),
    ]
