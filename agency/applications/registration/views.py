from django.shortcuts import render, redirect
from .forms import BusinessDetailForm, ContactPersonForm, CreditCardForm
from django.http import HttpResponse

def business_detail_view(request):
    if request.method == 'POST':
        form = BusinessDetailForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save()
            # Redirect to a new URL for adding contact persons and credit cards
            return redirect('add_contact_person', business_id=business.id)
    else:
        form = BusinessDetailForm()
    return render(request, 'registration/business_detail.html', {'form': form})

def add_contact_person(request, business_id):
    if request.method == 'POST':
        form = ContactPersonForm(request.POST)
        if form.is_valid():
            contact_person = form.save(commit=False)
            contact_person.business_id = business_id
            contact_person.save()
            # Redirect to allow adding another contact person or proceed to add credit cards
            return redirect('add_credit_card', business_id=business_id)  # Update this as needed
    else:
        form = ContactPersonForm()
    return render(request, 'registration/add_contact_person.html', {'form': form, 'business_id': business_id})

def add_credit_card(request, business_id):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            credit_card = form.save(commit=False)
            credit_card.business_id = business_id
            credit_card.save()
            # Redirect to review page or somewhere else as needed
            return HttpResponse("Credit Card added successfully! (Implement redirection)")  # Update this as needed
    else:
        form = CreditCardForm()
    return render(request, 'registration/add_credit_card.html', {'form': form, 'business_id': business_id})

