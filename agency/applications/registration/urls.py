from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.business_detail_view, name='register_business'),
]
