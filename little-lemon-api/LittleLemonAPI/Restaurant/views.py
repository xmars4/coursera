from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import MenuItem, Order, OrderItem
from .serializers import MenuItemSerializer, OrderItemSerializer
from .permissions import *

class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [AuthorizedEditDeleteMenuItem]


class OrderList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get(self, request):
        user_id = request.user.id
        orders = Order.objects.all().filter(user__id=user_id)
        order_items = OrderItem.objects.all().filter(order__in=orders)
        serialized_order_items = OrderItemSerializer(order_items, many=True)
        return Response(serialized_order_items.data)
