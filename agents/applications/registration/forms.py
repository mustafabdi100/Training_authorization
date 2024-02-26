from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BusinessDetail, ContactPerson, CreditCard
from django.forms import inlineformset_factory

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Remove help texts
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class BusinessDetailForm(forms.ModelForm):
    class Meta:
        model = BusinessDetail
        exclude = ('reference_number', 'status')

ContactPersonFormSet = inlineformset_factory(
    BusinessDetail, ContactPerson,
    fields=('first_name', 'last_name', 'mobile_number', 'email_address'),
    extra=3, max_num=3,
    can_delete=False  # Set can_delete to False to remove the "Delete" checkbox
)

CreditCardFormSet = inlineformset_factory(
    BusinessDetail, CreditCard,
    fields=('card_type', 'last_8_digits'),
    extra=3, max_num=3,
    can_delete=False  # Set can_delete to False to remove the "Delete" checkbox
)
