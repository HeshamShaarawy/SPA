from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('treatments/', views.treatments_index, name='treatments_index'),
    path('treatments/<int:treatment_id>/',
         views.treatments_detail, name='treatments_detail'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('treatments/', views.treatments_index, name='treatments_index'),
    path('treatments/<int:treatment_id>/',
         views.treatments_detail, name='treatments_detail'),
    path('treatments/create/', views.TreatmentCreate.as_view(),
         name='treatments_create'),
    path('treatments/<int:pk>/update/',
         views.TreatmentUpdate.as_view(), name='treatments_update'),
    path('treatments/<int:pk>/delete/',
         views.TreatmentDelete.as_view(), name='treatments_delete'),
    path('bookings/', views.bookings_index, name='bookings_index'),
    path('bookings/<int:booking_id>/',
         views.bookings_detail, name='bookings_detail'),
    path('bookings/create/', views.BookingCreate.as_view(), name='bookings_create'),
    path('bookings/<int:pk>/update/',
         views.BookingUpdate.as_view(), name='bookings_update'),
    path('bookings/<int:pk>/delete/',
         views.BookingDelete.as_view(), name='bookings_delete'),

    path('clients/', views.clients_index, name='clients_index'),
    path('clients/<int:client_id>/', views.clients_detail, name='clients_detail'),
    path('clients/create/', views.ClientCreate.as_view(),
         name='clients_create'),
    path('clients/<int:pk>/update/',
         views.ClientUpdate.as_view(), name='clients_update'),
    path('clients/<int:pk>/delete/',
         views.ClientDelete.as_view(), name='clients_delete'),


    #Authorizarion and registration
    path('accounts/signup/', views.signup, name='signup'),
    #filters
    path('search/', views.treatments_search, name='treatments_search')

]
