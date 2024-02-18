from django import forms
from .models import BusinessDetail,ContactPerson,CreditCard

class BusinessDetailForm(forms.ModelForm):
    class Meta:
        model = BusinessDetail
        fields = '__all__'
        widgets = {
            'registration_certificate': forms.FileInput(attrs={'accept': 'application/pdf'}),
            'trading_license': forms.FileInput(attrs={'accept': 'application/pdf'}),
            'tax_compliance_certificate': forms.FileInput(attrs={'accept': 'application/pdf'}),
        }

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = ['first_name', 'last_name', 'mobile_number', 'email_address']

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_type', 'last_8_digits']