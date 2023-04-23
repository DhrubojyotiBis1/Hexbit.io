from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Customer

# Create your views here.

ORDER = 'order_id'

@api_view(['GET'])
def View(request):
    data = request.data
    if not data.__contains__(ORDER):
        return Response({'status': 403, 'message': 'Order Id not found'})
    
    if Customer.objects.filter(order_id=data[ORDER]).exists():
        customer = Customer.objects.filter(order_id=data[ORDER]).values()
        return Response({'status': 200, 'customers': customer})

    else:
        return Response({'status': 404, 'message': 'No Customer Found'})
    
    
    