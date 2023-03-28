import json
from datetime import datetime


from rest_framework.decorators import api_view
from rest_framework.response import Response

from order_details.models import OrderDetails


SUCESS = 'Sucess'
FAIL = 'Fail'


#Helper Function
def getdataFromRequest(request):
    body = request.body
    return json.loads(body)


#API Functions
@api_view(['GET'])
def getOrders(request):
    data = getdataFromRequest(request)

    #TODO: Check authenticated user using JWT

    if not data.__contains__('pids'):
        return Response({'message': FAIL}, 400)
    
    orders = {}

    #TODO: Check if authenticated user is allowed to get order the data
    for pid in data['pids']:
        if OrderDetails.object.filter(productId=pid).exists():
            ordersForPid = OrderDetails.object.filter(productId=pid).values()
            orders[pid] = ordersForPid

    return Response({'message': SUCESS, 'orders': orders})


@api_view(['PUT'])
def updateOrders(request):
    data = getdataFromRequest(request)

    #TODO: Check authenticated user using JWT

    if not data.__contains__('ids'):
        return Response({'message': FAIL}, 400)
    
    #TODO: Check if authenticated user is allowed to update the order data
    for id in data['ids']:
        if OrderDetails.object.filter(pk=id).exists():
            orderDetails =  OrderDetails.object.get(pk=id)
            orderDetails.shipedDate = datetime.now()
            OrderDetails.object.save(orderDetails)
    
    return Response({'message': SUCESS}, 200)

    