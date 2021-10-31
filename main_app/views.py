from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Treatment, Booking, Client


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('treatments_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


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


class TreatmentCreate(CreateView):
    model = Treatment
    fields = ['name', 'image', 'category', 'description', 'price']
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


class BookingUpdate(UpdateView):
    model = Booking
    fields = '__all__'


class BookingDelete(DeleteView):
    model = Booking
    success_url = '/bookings/'

# Clients views


def clients_index(request):
    clients = Client.objects.all()
    print(clients)
    return render(request, 'clients/index.html', {'clients': clients})


def clients_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'clients/detail.html', {'client': client})


class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    success_url = '/clients/'


class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'


class ClientDelete(DeleteView):
    model = Client
    success_url = '/clients/'
