from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import *
from django.contrib.auth.models import User, Group


class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [AuthorizedManager]


class UserManagerView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialier
    permission_classes = [AuthorizedManager]

    def get(self, request):
        managers = User.objects.all().filter(groups__name='Manager')
        serialized_managers = UserSerialier(managers, many=True)
        return Response(serialized_managers.data)

    def post(self, request):
        username = request.data.get('username')
        user = get_object_or_404(User, username=username)
        manager_group = Group.objects.all().filter(name='Manager').first()
        user.groups.add(manager_group.id)
        return HttpResponse(status=201)

    def delete(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        manager_group = Group.objects.all().filter(name='Manager').first()
        user.groups.remove(manager_group.id)
        return HttpResponse(status=200)


class UserDeliveryCrewView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialier
    permission_classes = [AuthorizedManager]

    def get(self, request):
        managers = User.objects.all().filter(groups__name='Delivery crew')
        serialized_managers = UserSerialier(managers, many=True)
        return Response(serialized_managers.data)

    def post(self, request):
        username = request.data.get('username')
        user = get_object_or_404(User, username=username)
        manager_group = Group.objects.all().filter(name='Delivery crew').first()
        user.groups.add(manager_group.id)
        return HttpResponse(status=201)

    def delete(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        manager_group = Group.objects.all().filter(name='Delivery crew').first()
        user.groups.remove(manager_group.id)
        return HttpResponse(status=200)


# ===== Cart ====
class CartView(generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        current_cart_items = Cart.objects.all().filter(user=user)
        serialized_cart_items = CartSerializer(current_cart_items, many=True)
        return Response(serialized_cart_items.data)

    def post(self, request):
        menuitem_id = request.data.get('menuitem_id')
        quantity = request.data.get('quantity')
        menuitem = get_object_or_404(MenuItem, pk=menuitem_id)
        new_cart = CartSerializer(data={
            "user": request.user.id,
            "menuitem": menuitem.id,
            "quantity": quantity,
            "unit_price": menuitem.price,
            "price": menuitem.price * quantity
        })
        if new_cart.is_valid():
            new_cart.save()
            return Response(new_cart.data)
        return Response(new_cart.errors, status=400)

    def delete(self, request):
        user = request.user
        current_cart_items = Cart.objects.all().filter(user=user)
        current_cart_items.delete()
        return Response()


class OrderList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get(self, request):
        user_id = request.user.id
        orders = Order.objects.all().filter(user__id=user_id)
        order_items = OrderItem.objects.all().filter(order__in=orders)
        serialized_order_items = OrderItemSerializer(order_items, many=True)
        return Response(serialized_order_items.data)
