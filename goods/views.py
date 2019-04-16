from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Goods, Categories
from orders.models import Order
from purchasing.settings import BASE_DIR

from django.views.generic import ListView
# Create your views here.


class GoodsListView(ListView):
    model = Goods
    template_name = 'goods_list.html'
    context_object_name = 'goods'
    paginate_by = 10
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
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
            left_pages = range(current_page-around_count, current_page)

        if current_page+around_count >= pages_count-1:
            right_pages = range(current_page+1, pages_count+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1, current_page+around_count+1)

        return {'left_pages': left_pages,
                'right_pages': right_pages,
                'left_has_more': left_has_more,
                'right_has_more': right_has_more,}


def index(request):
    return render(request, 'index.html')


def search(request):
    goods_name = request.POST.get('goods_name')
    search_type = request.POST.get('search_type')
    if search_type == '1' and goods_name:
        goods = Goods.objects.filter(goods_name__contains=goods_name)
        return render(request, 'search.html', context={'goods': goods})
    elif search_type == '2' and goods_name:
        # orders = Order.objects.filter(user)
        print('search order')
        return redirect(reverse('index'))
    return redirect(reverse('index'))


def add(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        print('#'*30)
        print(categories)
        return render(request, 'add.html', context={'categories': categories})
    else:
        goods_name = request.POST.get('goods_name')
        goods_price_in = request.POST.get('goods_price_in')
        goods_price_out = request.POST.get('goods_price_out')
        goods_desc = request.POST.get('goods_desc')
        goods_address = request.POST.get('goods_address')
        category_id = request.POST.get('goods_categories')
        # goods_photo = request.POST.get('goods_photo')
        import os
        file_obj = request.FILES.get('goods_photo')
        print(type(file_obj))
        print(file_obj.name)
        with open(os.path.join(BASE_DIR, 'goods', 'static', file_obj.name), 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        goods_category = Categories.objects.get(pk=category_id)
        goods = Goods(goods_name=goods_name, goods_price_in=goods_price_in, goods_price_out=goods_price_out,
                      goods_desc=goods_desc, goods_address=goods_address, goods_category=goods_category,
                      goods_photo=file_obj.name)
        goods.save()
        return redirect(reverse('index'))
