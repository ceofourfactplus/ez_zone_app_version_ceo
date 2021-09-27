from pos.models import Order,OrderItem,OrderItemTopping
from pos.serializers import OrderSerializer, OrderItemSerializer, OrderItemToppingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class OrderList(APIView):
    def get(self, request):
        Orders = Order.objects.all()
        serializer = OrderSerializer(Orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OrderDetail(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise 404

    def get(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderSerializer(Order)
        return Response(serializer.data)

    def put(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderSerializer(Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Order = self.get_object(pk)
        Order.delete()
        return Response(status=204)

class OrderItemList(APIView):
    def get(self, request):
        Orders = OrderItem.objects.all()
        serializer = OrderItemSerializer(Orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OrderItemDetail(APIView):
    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            raise 404

    def get(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemSerializer(Order)
        return Response(serializer.data)

    def put(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemSerializer(Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Order = self.get_object(pk)
        Order.delete()
        return Response(status=204)

class OrderItemToppingList(APIView):
    def get(self, request):
        Orders = OrderItemTopping.objects.all()
        serializer = OrderItemToppingSerializer(Orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OrderItemToppingDetail(APIView):
    def get_object(self, pk):
        try:
            return OrderItemTopping.objects.get(pk=pk)
        except OrderItemTopping.DoesNotExist:
            raise 404

    def get(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemToppingSerializer(Order)
        return Response(serializer.data)

    def put(self, request, pk):
        Order = self.get_object(pk)
        serializer = OrderItemToppingSerializer(Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Order = self.get_object(pk)
        Order.delete()
        return Response(status=204)
