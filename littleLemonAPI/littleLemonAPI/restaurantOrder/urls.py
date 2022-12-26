from django.urls import path
from .views import MenuItem

urlpatterns = [
    path('menu-items/', MenuItem.as_view()),
]