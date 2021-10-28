from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('treatments/', views.treatments_index, name='treatments_index'),
    path('treatments/<int:treatment_id>/',
         views.treatments_detail, name='treatments_detail'),
    path('clients/', views.clients_index, name='client_detail'),
]
