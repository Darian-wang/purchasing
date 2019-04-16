from django.db import models

# Create your models here.


class Categories(models.Model):
    categories_name = models.CharField(max_length=100)

    class META:
        db_table = 'categories'


class Goods(models.Model):
    goods_name = models.CharField(max_length=200)
    goods_price_in = models.FloatField()
    goods_price_out = models.FloatField()
    goods_desc = models.CharField(max_length=10000)
    goods_address = models.CharField(max_length=1000)
    goods_category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    goods_photo = models.CharField(max_length=1000)

    class META:
        db_table = 'goods'


