from .import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('flight/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('user/<int:user_id>/', views.all_my_bookings, name='my_bookings'),
    path('user/<int:user_id>/booking/<int:booking_id>/',
         views.booking_detail, name='booking_detail'),
    path('user/<int:user_id>/journey/<int:journey_id>/remove/',
    views.my_journey_delete, name='my_journey_delete'),
]
