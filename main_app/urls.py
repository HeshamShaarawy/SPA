from django.urls import path, include
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('treatments/', views.treatments_index, name='treatments_index'),
path('treatments/<int:treatment_id>/', views.treatments_detail, name='treatments_detail'),
path('treatments/create/', views.TreatmentCreate.as_view(), name='treatments_create'),
path('treatments/<int:pk>/update/', views.TreatmentUpdate.as_view(), name='treatments_update'),
path('treatments/<int:pk>/delete/', views.TreatmentDelete.as_view(), name='treatments_delete'),
path('bookings/', views.bookings_index, name='bookings_index'),
path('bookings/<int:booking_id>/', views.bookings_detail, name='bookings_detail'),
path('bookings/create/', views.BookingCreate.as_view(), name='bookings_create'),
# path('bookings/<int:pk>/update/', views.BookingUpdate.as_view(), name='bookings_update'),
path('bookings/<int:pk>/delete/', views.BookingDelete.as_view(), name='bookings_delete'),
]