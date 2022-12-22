from django.urls import path, re_path
from .views import menu,display_menu_item,home, about,book

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name='about'),
    path('book/', book, name='book'),
    path('menu/', menu, name='menu'),
    path('menu_item/<int:pk>/', display_menu_item, name="menu_item"),
]