from rest_framework import serializers

from order_details.models import OrderDetails
from order.serializers import OrderSerializer


class OrderDetailsSerializer(serializers.ModelSerializer):
    #product = PoductSerializer()
    order = OrderSerializer()
    class Meta:
        model = OrderDetails
        fields = ['price', 'quantity', 'discount', 'total', 'shipedDate', 'order']

