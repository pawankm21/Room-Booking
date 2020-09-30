from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'accounts/index.html')


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    pass


def rooms(request):
    bookings = Booking.objects.all()
    room = Room.objects.all()
    user = User.objects.all()
    context = {'bookings': bookings, 'room': room, 'user': user}
    return render(request, 'accounts/rooms.html',context)
