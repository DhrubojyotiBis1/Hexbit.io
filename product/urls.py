from django.urls import path

from product import views


urlpatterns = [
    path('product-view/', views.getProducts, name='getProducts'),
    path('product-create/', views.postProducts, name='postProducts'),
    path('product-update/<int:pk>', views.updateProduct, name='updateProducts'),
    path('product-delete/', views.deleteProducts, name='deleteProducts'),
]