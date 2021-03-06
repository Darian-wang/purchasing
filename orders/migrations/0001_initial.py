# Generated by Django 2.2 on 2019-04-16 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_phone', models.CharField(max_length=13)),
                ('user_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('order_price', models.FloatField()),
                ('order_number', models.CharField(max_length=22)),
                ('express_number', models.CharField(max_length=100, null=True)),
                ('express_type', models.CharField(max_length=20, null=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.User')),
            ],
        ),
    ]
