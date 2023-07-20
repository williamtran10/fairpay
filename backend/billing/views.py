from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Order, Customer, Item
from .serializers import OrderSerializer, CustomerSerializer, BillSerializer, ItemSerializer
from decimal import Decimal


class Receipt:
    def __init__(self, table_id, customer_id, cost):
        self.table_id = table_id
        self.customer_id = customer_id
        self.cost = cost

    def __str__(self):
        return f"{self.table_id} {self.customer_id} {self.cost}"


def get_customer_order(customer_id):
    try:
        return Order.objects.filter(customer_id=customer_id)
    except Order.DoesNotExist:
        raise Http404


def get_customer(pk):
    try:
        return Customer.objects.get(id=pk)

    except Order.DoesNotExist:
        raise Http404

class OrderView(APIView):

    def post(self, request):
        data = request.data
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Order added", safe=False)
        return JsonResponse("Failed to add order", safe=False)

    def get_order(self, customer_id, item_id):
        try:
            return Order.objects.get(customer_id=customer_id, item_id=item_id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, customer_id=None, item_id=None):
        if item_id:
            data = self.get_order(customer_id, item_id)
            serializer = OrderSerializer(data)
        elif customer_id:
            data = get_customer_order(customer_id)
            serializer = OrderSerializer(data, many=True)
        else:
            data = Order.objects.all()
            serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, customer_id, item_id):
        order_to_update = Order.objects.get(customer_id=customer_id, item_id=item_id)
        serializer = OrderSerializer(instance=order_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Order updated", safe=False)
        return JsonResponse("Failed to update order")

    def delete(self, request, customer_id, item_id):
        order_to_delete = Order.objects.get(customer_id=customer_id, item_id=item_id)
        order_to_delete.delete()
        return JsonResponse("Order deleted", safe=False)


class CustomerView(APIView):

    def get(self, request, pk=None):
        if pk:
            data = get_customer(pk)
            serializer = CustomerSerializer(data)
        else:
            data = Customer.objects.all()
            serializer = CustomerSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        customer_to_update = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(instance=customer_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Customer updated", safe=False)
        return JsonResponse("Failed to update customer")


class BillView(APIView):
    def get(self, request, customer_id):
        customer = CustomerSerializer(get_customer(customer_id)).data
        orders = OrderSerializer(get_customer_order(customer_id), many=True).data
        items = ItemSerializer(Item.objects.all(), many=True).data
        item_prices = {}
        for item in items:
            item_prices[item['id']] = Decimal(item['cost'])

        total_cost = 0
        for order in orders:
            total_cost += item_prices[order['item_id']] * order['amount']
        total_cost += Decimal(customer['tip'])

        receipt = Receipt(int(customer['table_id']), int(customer_id), total_cost)
        serializer = BillSerializer(receipt)
        return Response(serializer.data)
