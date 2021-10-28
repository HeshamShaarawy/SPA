from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Treatment, Booking, Client


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

    # Treatments views


def treatments_index(request):
    treatments = Treatment.objects.all()
    return render(request, 'treatments/index.html', {'treatments': treatments})


def treatments_detail(request, treatment_id):
    treatment = Treatment.objects.get(id=treatment_id)
    return render(request, 'treatments/detail.html', {'treatment': treatment})

# Clients views
# def clients_index(request):


class TreatmentCreate(CreateView):
    model = Treatment
    fields = '__all__'
    # success_url = '/treatments/'


class TreatmentUpdate(UpdateView):
    model = Treatment
    fields = '__all__'


class TreatmentDelete(DeleteView):
    model = Treatment
    success_url = '/treatments/'

# bookings views


def bookings_index(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/index.html', {'bookings': bookings})


def bookings_detail(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'bookings/detail.html', {'booking': booking})


class BookingCreate(CreateView):
    model = Booking
    fields = '__all__'
    # success_url = '/bookings/'


class Bookingupdate(UpdateView):
    model = Booking
    fields = '__all__'


class BookingDelete(DeleteView):
    model = Booking
    success_url = '/bookings/'
