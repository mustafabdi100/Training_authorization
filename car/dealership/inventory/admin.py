from django.contrib import admin
from .models import Manufacturer, Vehicle, Image, Category

admin.site.register(Manufacturer)
admin.site.register(Image) 
admin.site.register(Category)

class VehicleAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

admin.site.register(Vehicle, VehicleAdmin)