from django.contrib import admin

from main_app.models import Treatment
from .models import Treatment

# Register your models here.
admin.site.register(Treatment)
