from django.urls import path,re_path
from .views import *

urlpatterns = [
    re_path('^menu-items/$', MenuItemList.as_view()),
    re_path('menu-items/(?P<pk>\d+)/$', MenuItemDetail.as_view()),
    path('orders', OrderList.as_view()),
    path("groups/manager/users", UserManagerView.as_view()),
    path("groups/manager/users/<int:pk>", UserManagerView.as_view()),
    path("groups/delivery-crew/users", UserDeliveryCrewView.as_view()),
    path("groups/delivery-crew/users/<int:pk>", UserDeliveryCrewView.as_view()),

]
