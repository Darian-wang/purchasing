from django.urls import path
from .views import index, search, add, GoodsListView


urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('add/', add, name='add'),
    path('list/', GoodsListView.as_view(), name='goods_list'),
]