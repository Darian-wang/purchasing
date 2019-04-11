from django.shortcuts import render, redirect, reverse
from .models import Goods
# Create your views here.


def index(request):
    return render(request, 'index.html')


def search(request):
    goods_name = request.POST.get('goods_name')
    if goods_name:
        goods = Goods.objects.filter(goods_name__contains=goods_name)
        return render(request, 'search.html', context={'goods': goods})
    return redirect(reverse('index'))
