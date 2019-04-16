from django.shortcuts import render
from goods.models import Goods
from .models import User, Order
from django.shortcuts import redirect, reverse
import time


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', context={'orders': orders})


def delete_order(request):
    order_id = request.GET.get('order_id')
    orders = Order.objects.get(pk=order_id)
    orders.delete()
    return redirect(reverse('orders:order_list'))


def add_order(request):
    if request.method == 'GET':
        goods = Goods.objects.all()
        return render(request, 'add_order.html', context={'goods': goods})
    else:
        user_name = request.POST.get('user_name')
        user_phone = request.POST.get('user_phone')
        user_address = request.POST.get('user_address')
        user = User(user_name=user_name, user_phone=user_phone,
                    user_address=user_address)
        print(user)
        user.save()
        goods_id = request.POST.get('goods_id')
        goods = Goods.objects.get(pk=goods_id)
        order_price = request.POST.get('order_price')
        now = time.strftime('%Y%m%d%H%M%S', time.localtime())

        # order_last = Order.objects.aggregate(Max('order_number'))
        # order_number = '{}'.format(now,)

        order = Order(user=user, goods=goods, order_price=order_price,
                      order_number=now)
        order.save()
        return redirect(reverse('orders:order_list'))
