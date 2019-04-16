from django.urls import path
from .views import add_order, order_list, delete_order, is_buy, order_list_on_bought

app_name = 'orders'

urlpatterns = [
    path('', order_list, name='order_list'),
    path('add_order/', add_order, name='add_order'),
    path('delete_order/', delete_order, name='delete_order'),
    path('is_buy/', is_buy, name='is_buy'),
    path('order_list_on_bought/', order_list_on_bought, name='order_list_on_bought'),
]