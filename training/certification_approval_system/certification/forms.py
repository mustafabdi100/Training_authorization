# certification/forms.py

from django import forms
from .models import EmployeeRequest, Feedback,BondAgreement

class EmployeeRequestForm(forms.ModelForm):
    class Meta:
        model = EmployeeRequest
        fields = ['name', 'department', 'reason_for_request']

class HRFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['recipient_name', 'recipient_email', 'sent_date', 'department', 'feedback_text']

class BondAgreementForm(forms.ModelForm):
    class Meta:
        model = BondAgreement
        fields = [
            'employee_name',
            'department',
            'contract_terms',
        ]
