from rest_framework import serializers
from .models import Item, Customer, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id',
                  'name',
                  'cost')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id',
                  'table_id',
                  'tip')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer_id',
                  'item_id',
                  'amount')


class BillSerializer(serializers.Serializer):
    class Meta:
        fields = ('table_id',
                  'customer_id',
                  'cost')

    table_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()
    cost = serializers.DecimalField(max_digits=6, decimal_places=2)