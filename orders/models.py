from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=13)
    user_address = models.CharField(max_length=200)

    def __str__(self):
        return '<{}>({}, {}, {})'.format(self.__class__.__name__,
                                         self.user_name, self.user_phone,
                                         self.user_address)


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    goods = models.ForeignKey('goods.Goods', on_delete=models.CASCADE)
    order_price = models.FloatField()
    order_number = models.CharField(max_length=22)
    create_time = models.DateTimeField(auto_now=True)
    express_number = models.CharField(max_length=100, null=True)
    express_type = models.CharField(max_length=20, null=True)
