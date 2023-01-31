from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # def get(self, request):
    #     ...
    #
    # def post(self, request):
    #     ...


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # def get(self, request):
    #     ...
    #
    # def put(self, request):
    #     ...
    #
    # def delete(self, request):
    #     ...
