from pos.models import Order, OrderItem, OrderItemTopping
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','status_delivery','total_price','total_amount','sale_channel','customer_name','descriptions','status_order']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','flavour_level','flavour_type','product','order','total_price','descriptions','amount']

class OrderItemToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemTopping
        fields = ['id','item','topping','total_price','amount']