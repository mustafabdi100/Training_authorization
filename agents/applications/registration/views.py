import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,permission_required
from .forms import BusinessDetailForm, ContactPersonFormSet, CreditCardFormSet, CustomUserCreationForm
from .models import BusinessDetail, ActivityLog

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            ActivityLog.objects.create(user=user, action='add_user', description='User registered.')
            return redirect('dashboard_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def business_detail_view(request):
    if request.method == 'POST':
        form = BusinessDetailForm(request.POST, request.FILES)
        if form.is_valid():
            business_detail = form.save()
            ActivityLog.objects.create(user=request.user, action='submission', description=f'Business detail submitted for {business_detail.business_name}.')
            return redirect('contact_person_view', business_id=business_detail.id)
    else:
        form = BusinessDetailForm()
    return render(request, 'registration/business_detail.html', {'form': form})

@login_required
def contact_person_view(request, business_id):
    business_detail = BusinessDetail.objects.get(id=business_id)
    if request.method == "POST":
        formset = ContactPersonFormSet(request.POST, instance=business_detail)
        if formset.is_valid():
            formset.save()
            ActivityLog.objects.create(user=request.user, action='update', description=f'Contact persons updated for {business_detail.business_name}.')
            return redirect('credit_card_view', business_id=business_id)
    else:
        formset = ContactPersonFormSet(instance=business_detail)
    return render(request, 'registration/contact_person.html', {'formset': formset, 'business_id': business_id})

@login_required
def credit_card_view(request, business_id):
    business_detail = BusinessDetail.objects.get(id=business_id)
    if request.method == "POST":
        formset = CreditCardFormSet(request.POST, instance=business_detail)
        if formset.is_valid():
            formset.save()
            ActivityLog.objects.create(user=request.user, action='update', description=f'Credit card info updated for {business_detail.business_name}.')
            return redirect('review_application', business_id=business_id)
    else:
        formset = CreditCardFormSet(instance=business_detail)
    return render(request, 'registration/credit_card.html', {'formset': formset, 'business_id': business_id})

@login_required
def review_application(request, business_id):
    business_detail = get_object_or_404(BusinessDetail, id=business_id)
    if request.method == "POST":
        if 'approve' in request.POST:
            business_detail.status = 'approved'
            business_detail.save()
            ActivityLog.objects.create(user=request.user, action='approval', description=f'Application for {business_detail.business_name} approved.')
            return redirect('dashboard_view')
        elif 'reject' in request.POST:
            business_detail.status = 'rejected'
            business_detail.save()
            ActivityLog.objects.create(user=request.user, action='rejection', description=f'Application for {business_detail.business_name} rejected.')
            return redirect('dashboard_view')
    contact_persons = business_detail.contact_persons.all()
    credit_cards = business_detail.credit_cards.all()
    context = {'business_detail': business_detail, 'contact_persons': contact_persons, 'credit_cards': credit_cards}
    return render(request, 'registration/review_application.html', context)

def generate_unique_reference():
    while True:
        reference = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if not BusinessDetail.objects.filter(reference_number=reference).exists():
            return reference

@login_required
def final_submission_view(request, business_id):
    business_detail = get_object_or_404(BusinessDetail, id=business_id)
    reference_number = generate_unique_reference()
    business_detail.reference_number = reference_number
    business_detail.save()
    
    ActivityLog.objects.create(user=request.user, action='final_submission', description=f'Final submission for application with reference number {reference_number} completed.')
    
    return redirect('submission_success', reference_number=reference_number)


@login_required
def submission_success_view(request, reference_number):
    context = {'reference_number': reference_number}
    return render(request, 'registration/submission_success.html', context)

@login_required
def dashboard_view(request):
    total_applications = BusinessDetail.objects.count()
    pending_applications = BusinessDetail.objects.filter(status='pending').count()
    approved_applications = BusinessDetail.objects.filter(status='approved').count()
    rejected_applications = BusinessDetail.objects.filter(status='rejected').count()
    all_applications = BusinessDetail.objects.all()
    context = {
        'total_applications': total_applications,
        'pending_applications': pending_applications,
        'approved_applications': approved_applications,
        'rejected_applications': rejected_applications,
        'all_applications': all_applications,
    }
    return render(request, 'registration/dashboard.html', context)

@login_required
def pending_applications_view(request):
    pending_applications = BusinessDetail.objects.filter(status='pending')
    return render(request, 'registration/pending_applications.html', {'pending_applications': pending_applications})

@login_required
def approved_applications_view(request):
    approved_applications = BusinessDetail.objects.filter(status='approved')
    return render(request, 'registration/approved_applications.html', {'approved_applications': approved_applications})

@login_required
def rejected_applications_view(request):
    rejected_applications = BusinessDetail.objects.filter(status='rejected')
    return render(request, 'registration/rejected_applications.html', {'rejected_applications': rejected_applications})

@login_required
def application_review_view(request, application_id):
    application = get_object_or_404(BusinessDetail, id=application_id)
    is_rejected = application.status == 'rejected'
    
    if request.method == "POST":
        if 'approve' in request.POST and not is_rejected:
            application.status = 'approved'
            application.save()
            ActivityLog.objects.create(user=request.user, action='approval', description=f'Application with reference number {application.reference_number} approved.')
            return redirect('dashboard_view')
        elif 'reject' in request.POST and not is_rejected:
            application.status = 'rejected'
            application.save()
            ActivityLog.objects.create(user=request.user, action='rejection', description=f'Application with reference number {application.reference_number} rejected.')
            return redirect('dashboard_view')
    
    context = {
        'application': application,
        'is_rejected': is_rejected,
    }
    return render(request, 'registration/application_review.html', context)


@login_required
def reject_application(request, application_id):
    application = get_object_or_404(BusinessDetail, id=application_id)
    application.status = 'rejected'
    application.save()
    ActivityLog.objects.create(user=request.user, action='rejection', description=f'Application {application_id} rejected.')
    return redirect('approved_applications_view')



@login_required
@permission_required('yourapp.view_activitylog', raise_exception=True)
def view_activity_logs(request):
    logs = ActivityLog.objects.all().order_by('-timestamp')
    return render(request, 'registration/view_activity_logs.html', {'logs': logs})