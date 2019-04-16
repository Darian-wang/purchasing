from django.urls import path
from .views import add_order, order_list, delete_order

app_name = 'orders'

urlpatterns = [
    path('', order_list, name='order_list'),
    path('add_order/', add_order, name='add_order'),
    path('delete_order/', delete_order, name='delete_order'),
]