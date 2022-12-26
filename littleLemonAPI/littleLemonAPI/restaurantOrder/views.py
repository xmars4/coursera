from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItem(View):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        pass
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass
