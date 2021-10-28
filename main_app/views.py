from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Treatment


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
