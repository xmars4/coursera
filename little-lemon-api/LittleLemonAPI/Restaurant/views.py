from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
