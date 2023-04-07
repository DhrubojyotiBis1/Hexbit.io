from django.urls import path
from . import views

urlpatterns = [
    path('get_customer/', views.get_customer, name="GetCustomer"),
]