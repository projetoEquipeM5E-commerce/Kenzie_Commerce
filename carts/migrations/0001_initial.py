# Generated by Django 4.2.2 on 2023-07-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['cart_id'],
            },
        ),
    ]