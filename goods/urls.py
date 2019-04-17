from django.urls import path
from .views import index, add_goods, delete_goods, modify_goods, GoodsListView


urlpatterns = [
    path('', index, name='index'),
    path('add_goods/', add_goods, name='add_goods'),
    path('delete_goods/', delete_goods, name='delete_goods'),
    path('modify_goods/', modify_goods, name='modify_goods'),
    path('goods_list/', GoodsListView.as_view(), name='goods_list'),
]