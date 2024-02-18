from django.db import models

class BusinessDetail(models.Model):
    business_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100)
    kra_pin = models.CharField(max_length=50)
    business_address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    registration_certificate = models.FileField(upload_to='documents/')
    trading_license = models.FileField(upload_to='documents/')
    tax_compliance_certificate = models.FileField(upload_to='documents/')

class ContactPerson(models.Model):
    business = models.ForeignKey(BusinessDetail, related_name='contact_persons', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email_address = models.EmailField()

class CreditCard(models.Model):
    business = models.ForeignKey(BusinessDetail, related_name='credit_cards', on_delete=models.CASCADE)
    card_type = models.CharField(max_length=50, choices=[('Visa', 'Visa'), ('MasterCard', 'MasterCard'), ('American Express', 'American Express')])
    last_8_digits = models.CharField(max_length=8)
