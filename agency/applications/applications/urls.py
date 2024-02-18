
from django.contrib import admin
from django.urls import path,include
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('registration/', include('registration.urls')),
       path('add-contact-person/<int:business_id>/', views.add_contact_person, name='add_contact_person'),
    path('add-credit-card/<int:business_id>/', views.add_credit_card, name='add_credit_card'),
]
