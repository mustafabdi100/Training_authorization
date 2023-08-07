# certification/views.py

from django.shortcuts import render, redirect,get_object_or_404
from .models import EmployeeRequest, Feedback,BondAgreement
from .forms import EmployeeRequestForm, HRFeedbackForm,BondAgreementForm

def employee_dashboard(request):
    employee_requests = EmployeeRequest.objects.filter(status='Approved')
    
    # Dummy email to filter feedbacks (you can change it to any value you want)
    dummy_email = 'dummy@example.com'
    feedbacks = Feedback.objects.filter(recipient_email=dummy_email)
    
    context = {
        'employee_requests': employee_requests,
        'feedbacks': feedbacks,
    }
    return render(request, 'certification/employee_dashboard.html', context)

def approved_requests(request):
    approved_requests = EmployeeRequest.objects.filter(status='Approved')
    return render(request, 'certification/approved.html', {'approved_requests': approved_requests})

def pending_requests(request):
    requests = EmployeeRequest.objects.filter(status='Pending')
    return render(request, 'certification/pending.html', {'requests': requests})


def declined_requests(request):
    declined_requests = EmployeeRequest.objects.filter(status='Declined')
    return render(request, 'certification/declined.html', {'declined_requests': declined_requests})

def new_request(request):
    if request.method == 'POST':
        form = EmployeeRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pending_requests')  # Corrected URL pattern name
    else:
        form = EmployeeRequestForm()

    return render(request, 'certification/new_request.html', {'form': form})

def hr_dashboard(request):

  all_requests = EmployeeRequest.objects.all()  
  pending_requests = EmployeeRequest.objects.filter(status='Pending')
  approved_requests = EmployeeRequest.objects.filter(status='Approved')
  declined_requests = EmployeeRequest.objects.filter(status='Declined')

  context = {
    'all_requests': all_requests,
    'pending_requests': pending_requests,
    'approved_requests': approved_requests, 
    'declined_requests': declined_requests
  }

  return render(request, 'certification/hr_dashboard.html', context)

def hr_all_requests(request):
  all_requests = EmployeeRequest.objects.all()

  context = {
    'all_requests': all_requests
  }

  return render(request, 'certification/hr_all_requests.html', context)

def hr_pending_requests(request):
    # Get all pending requests
    pending_requests = EmployeeRequest.objects.filter(status='Pending')
    context = {
        'pending_requests': pending_requests,
    }
    return render(request, 'certification/hr_pending.html', context)

def hr_approve_request(request, request_id):
    # Get the certification request by id
    certification_request = get_object_or_404(EmployeeRequest, id=request_id)

    if request.method == 'POST':
        # Process the form submission for approval
        certification_request.status = 'Approved'
        certification_request.save()

        # Redirect back to HR pending requests
        return redirect('hr_pending_requests')

    context = {
        'request': certification_request,
    }
    return render(request, 'certification/hr_approve.html', context)


def hr_decline_request(request, request_id):
    # Get the certification request by id
    certification_request = get_object_or_404(EmployeeRequest, id=request_id)

    if request.method == 'POST':
        # Process the form submission for declining
        certification_request.status = 'Declined'
        certification_request.save()

        # Redirect back to HR pending requests
        return redirect('hr_pending_requests')

    context = {
        'request': certification_request,
    }
    return render(request, 'certification/hr_decline.html', context)

def hr_approved_requests(request):
    approved_requests = EmployeeRequest.objects.filter(status='Approved').prefetch_related('bondagreement_set')
    context = {
        'approved_requests': approved_requests
    }
    return render(request, 'certification/hr_approved_requests.html', context)

def hr_declined_requests(request):
  declined_requests = EmployeeRequest.objects.filter(status='Declined')

  context = {
    'declined_requests': declined_requests
  }

  return render(request, 'certification/hr_declined_requests.html', context)

def send_bond_agreement(request, request_id):
    employee_request = get_object_or_404(EmployeeRequest, id=request_id)

    if request.method == 'POST':
        form = BondAgreementForm(request.POST)
        if form.is_valid():
            bond_agreement = form.save(commit=False)
            bond_agreement.employee_name = employee_request.name
            bond_agreement.department = employee_request.department
            bond_agreement.save()

            # Mark the original request as sent
            employee_request.sent_bond_agreement = True
            employee_request.save()

            return redirect('hr_approved_requests')  # Redirect back to the approved requests list
    else:
        form = BondAgreementForm()

    context = {
        'form': form,
        'employee_request': employee_request,
    }
    return render(request, 'certification/send_bond_agreement.html', context)

def view_bond_agreement(request, bond_agreement_id):
    bond_agreement = get_object_or_404(BondAgreement, id=bond_agreement_id)

    if request.method == 'POST':
        # Logic for employee signing the agreement goes here
        bond_agreement.is_signed = True
        bond_agreement.save()
        return redirect('employee_dashboard')

    context = {
        'bond_agreement': bond_agreement,
    }
    return render(request, 'certification/view_bond_agreement.html', context)

def employee_decline_bond_agreement(request, bond_agreement_id):
    bond_agreement = get_object_or_404(BondAgreement, id=bond_agreement_id)

    # Add your decline logic here if needed

    # For simplicity, let's mark the agreement as declined
    bond_agreement.is_signed = False
    bond_agreement.save()

    return redirect('employee_dashboard')
