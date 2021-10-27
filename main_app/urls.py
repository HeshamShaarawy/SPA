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

]