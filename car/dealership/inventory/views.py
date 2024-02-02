from django.shortcuts import render,get_object_or_404
from .models import Vehicle,Manufacturer

def index(request):
    vehicles = Vehicle.objects.all() 
    return render(request, 'inventory/index.html', {'vehicles': vehicles}) 

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'inventory/detail.html', {'vehicle': vehicle})

def manufacturer_detail(request, pk):
    manufacturer = Manufacturer.objects.get(pk=pk)
    vehicles = manufacturer.vehicle_set.order_by('year','model') 
    return render(request, 'inventory/manufacturer_detail.html', {'manufacturer': manufacturer, 'vehicles': vehicles})

def manufacturer_index(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturers/index.html', {'manufacturers': manufacturers})

def vehicle_list(request):
    categories = request.GET.getlist('category')
    vehicles = Vehicle.objects.all()
    if categories:
        vehicles = vehicles.filter(categories__in=categories)
    context = {'vehicles': vehicles}
    return render(request, 'inventory/vehicle_list.html', context)