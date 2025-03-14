from .import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('flight/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('my_booking/<int:user_id>/', views.my_booking, name='my_booking'),
    path('my_booking/<int:user_id>/journey/<int:journey_id>/remove/',
    views.my_journey_delete, name='my_journey_delete'),
]
