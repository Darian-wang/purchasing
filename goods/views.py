from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Goods, Categories
from purchasing.settings import BASE_DIR
# Create your views here.


def index(request):
    return render(request, 'index.html')


def search(request):
    goods_name = request.POST.get('goods_name')
    if goods_name:
        goods = Goods.objects.filter(goods_name__contains=goods_name)
        return render(request, 'search.html', context={'goods': goods})
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
        return HttpResponse('添加商品成功')
