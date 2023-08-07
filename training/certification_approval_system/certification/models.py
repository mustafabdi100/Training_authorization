from django.db import models

DEPARTMENT_CHOICES = [
    ('HR', 'HR'),
    ('Marketing', 'Marketing & Sales'),
    ('Software Development', 'Software Development'),
    ('Cyber Security', 'Cyber Security'),
    ('Networking', 'Networking'),
    ('Finance', 'Finance'),
    ('Data Analysis', 'Data Analysis'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
]

class EmployeeRequest(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    request_date = models.DateField(auto_now_add=True)
    reason_for_request = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    

    def __str__(self):
        return self.name

class Feedback(models.Model):
    sender = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    recipient_email = models.EmailField()
    sent_date = models.DateField()
    department = models.CharField(max_length=100)
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback from {self.sender} to {self.recipient_name}"
    


class BondAgreement(models.Model):
   employee_request = models.ForeignKey(EmployeeRequest, on_delete=models.CASCADE, default=1)
   employee_name = models.CharField(max_length=50)
   department = models.CharField(max_length=50)
   contract_terms = models.TextField()

   is_signed = models.BooleanField(default=False)

   def __str__(self):
        return f"Bond Agreement for {self.employee_request.name}"

