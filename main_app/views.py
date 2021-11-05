from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .choices import price_choices
from .models import Treatment, Booking, Client
import datetime


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('treatments_index')
    else:
      error_message = 'Invalid information, check the requirements'
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
    #displaying number of pages specified per page
    paginator = Paginator(treatments, 4)
    page = request.GET.get('page')
    page_treatments = paginator.get_page(page)
    
    context = {
        'treatments': page_treatments,
        #for filtering
        'price_choices': price_choices
    }
    return render(request, 'treatments/index.html', context)


def treatments_detail(request, treatment_id):
    treatment = Treatment.objects.get(id=treatment_id)
    return render(request, 'treatments/detail.html', {'treatment': treatment})


class TreatmentCreate(LoginRequiredMixin, CreateView):
    model = Treatment
    fields = ['name', 'image', 'category', 'description', 'price']
    # success_url = '/treatments/'



class TreatmentUpdate(LoginRequiredMixin, UpdateView):
    model = Treatment
    fields = '__all__'



class TreatmentDelete(LoginRequiredMixin,DeleteView):
    model = Treatment
    success_url = '/treatments/'

# bookings views


@login_required
def bookings_index(request):
    bookings = Booking.objects.all()
    bookings = bookings.order_by('date')
    
    date = datetime.date.today()
     #displaying number of pages specified per page
    paginator = Paginator(bookings, 10)
    page = request.GET.get('page')
    page_bookings = paginator.get_page(page)
    context = { 'bookings' : page_bookings, 'date' : date}
    return render(request, 'bookings/index.html',  context)


@login_required
def bookings_detail(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'bookings/detail.html', {'booking': booking})



class BookingCreate(LoginRequiredMixin, CreateView):
    model = Booking
    fields = '__all__'
    success_url = '/bookings/'



class BookingUpdate(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = '__all__'



class BookingDelete(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = '/bookings/'

# Clients views


@login_required
def clients_index(request):
    clients = Client.objects.all()
    print(clients)
    return render(request, 'clients/index.html', {'clients': clients})


@login_required
def clients_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'clients/detail.html', {'client': client})


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    success_url = '/clients/'



class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'



class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = '/clients/'


#Filter views

@login_required
def treatments_search(request):
    queryset_list = Treatment.objects.all()
    #By name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)
      # By price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'treatments': queryset_list,
        'values': request.GET 
    }
    return render(request, 'treatments/search.html', context)


@login_required
def clients_search(request):
    queryset_list = Client.objects.all()
    #By First Name
    if 'firstname' in request.GET:
        firstname = request.GET['firstname']
        if firstname:
            queryset_list = queryset_list.filter(first_name__icontains=firstname)
      # By Last Name
    if 'lastname' in request.GET:
        lastname = request.GET['lastname']
        if lastname:
            queryset_list = queryset_list.filter(last_name__icontains=lastname)
    # By Phone number
    if 'phone' in request.GET:
        phone = request.GET['phone']
        if phone:
            queryset_list = queryset_list.filter(phone_number__iexact=phone)
    # By Email
    if 'email' in request.GET:
        email = request.GET['email']
        if email:
            queryset_list = queryset_list.filter(email_address__iexact=email)

    context = {
        'clients': queryset_list,
        'values': request.GET 
    }
    return render(request, 'clients/search.html', context)

@login_required
def bookings_search(request):
    queryset_list = Booking.objects.all()
    #By name
    if 'date' in request.GET:
        date = request.GET['date']
        if date:
            queryset_list = queryset_list.filter(date = date)
      # By price
    if 'time' in request.GET:
        time = request.GET['time']
        if time:
            queryset_list = queryset_list.filter(time = time)
    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            queryset_list = queryset_list.filter(status= status)
    if 'client' in request.GET:
        client = request.GET['client']
        if client:
            queryset_list = queryset_list.filter(client = client)

    context = {
        'bookings': queryset_list,
        'values': request.GET 
    }
    return render(request, 'bookings/search.html', context)