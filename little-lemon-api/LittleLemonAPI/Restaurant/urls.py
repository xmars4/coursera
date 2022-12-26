from django.urls import path,re_path
from .views import MenuItemList, MenuItemDetail

urlpatterns = [
    re_path('^menu-items/$', MenuItemList.as_view()),
    re_path('menu-items/(?P<pk>\d+)/$', MenuItemDetail.as_view()),
]
