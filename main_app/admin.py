from django.contrib import admin

from main_app.models import Treatment
from .models import Booking, Client, Treatment

# Register your models here.
admin.site.register(Treatment)
admin.site.register(Booking)
admin.site.register(Client)
