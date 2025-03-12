from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Flight


# Create your views here.
class HomePage(generic.ListView):
    """
    Displays the home page.
    """
    queryset = Flight.objects.all()
    template_name = 'booking/index.html'