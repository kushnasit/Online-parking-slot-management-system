from django.shortcuts import render
from .models import ParkingSlot

def home(request):
    return render(request, 'home.html')

def slots(request):
    slots = ParkingSlot.objects.all()
    return render(request, 'slots.html', {'slots': slots})

def booking(request):
    return render(request, 'booking.html')
