from orders.views import search_order_by_user_name
from goods.views import search_goods_by_goods_name
from django.http import HttpResponse


def search(request):
    search_name = request.POST.get('goods_name')
    search_type = request.POST.get('search_type')
    # 根据商品名称搜索，获取商品详情
    if search_type == '1':
        return search_goods_by_goods_name(request, search_name)
    # 根据用户名搜索，获取订单详情
    elif search_type == '2':
        return search_order_by_user_name(request, search_name)
