from django.urls import path

from order_details import views


urlpatterns = [
    path('view/', views.getOrders, name='getOrders'),
    path('update/', views.updateOrders, name='updateOrders')
]