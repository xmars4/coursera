# -*- coding:utf-8 -*-
from rest_framework.serializers import ModelSerializer
from .models import Menu
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
