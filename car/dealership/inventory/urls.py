from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:vehicle_id>', views.vehicle_detail, name='vehicle_detail'),
    path('manufacturers/', views.manufacturer_index, name='manufacturers'), 
    path('manufacturers/<int:pk>/', views.manufacturer_detail, name='manufacturer_detail'),
     path('inventory/', views.vehicle_list, name='vehicle-list'),
    


]