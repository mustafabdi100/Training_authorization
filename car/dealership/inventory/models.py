from django.db import models
from django.urls import reverse

class Category(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
       return self.name
  

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
     return reverse('manufacturer_detail', kwargs={'pk': self.pk})
    
class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.PositiveIntegerField()
    mileage = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}"
    
    def get_absolute_url(self):
     return reverse('vehicle_detail', kwargs={'vehicle_id': self.pk})

class Image(models.Model):
    img = models.ImageField(upload_to='photos')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Image {self.id} of {self.vehicle}"
