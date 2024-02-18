from django.contrib import admin
from .models import BusinessDetail, ContactPerson, CreditCard

class ContactPersonInline(admin.TabularInline):
    model = ContactPerson
    extra = 1  # Specifies the number of blank forms the formset should display.

class CreditCardInline(admin.TabularInline):
    model = CreditCard
    extra = 1

class BusinessDetailAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'registration_number', 'city', 'country', 'phone_number', 'email_address')
    inlines = [ContactPersonInline, CreditCardInline]

admin.site.register(BusinessDetail, BusinessDetailAdmin)
