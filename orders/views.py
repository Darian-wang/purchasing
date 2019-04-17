from django.shortcuts import render
from goods.models import Goods
from .models import User, Order
from django.shortcuts import redirect, reverse
from django.views.generic import ListView
from django.core.paginator import Paginator, Page
import time


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 10
    page_kwarg = 'page'
    ordering = '-create_time'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        print('#'*10)
        print(type(paginator.object_list))
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        pages_count = paginator.num_pages
        left_has_more = False
        right_has_more = False

        if current_page - around_count <= 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page + around_count >= pages_count - 1:
            right_pages = range(current_page + 1, pages_count + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {'left_pages': left_pages,
                'right_pages': right_pages,
                'left_has_more': left_has_more,
                'right_has_more': right_has_more, }


def delete_order(request):
    order_id = request.GET.get('order_id')
    orders = Order.objects.get(pk=order_id)
    orders.delete()
    return redirect(reverse('orders:order_list'))


def search_order_by_user_name(request, username):
    users = User.objects.filter(user_name__contains=username).all()
    orders = []
    for user in users:
        user_orders = user.order_set.all()
        orders.append(user_orders)
    return render(request, 'search_order.html', context={'orders': orders})


def order_list_on_bought(request):
    orders = Order.objects.filter(is_buy=False)
    return render(request, 'order_list.html', context={'orders': orders})


def is_buy(request):
    order_id = request.GET.get('order_id')
    orders = Order.objects.get(pk=order_id)

    buy = request.POST.get('is_buy')
    if buy == 'yes':
        orders.is_buy = False
    else:
        orders.is_buy = True
    orders.save()
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
