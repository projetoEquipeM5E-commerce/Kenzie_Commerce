# Generated by Django 4.2.2 on 2023-07-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('carts', models.ManyToManyField(related_name='products', to='carts.cart')),
                ('orders', models.ManyToManyField(related_name='products', to='orders.order')),
            ],
        ),
    ]
