# Generated by Django 3.1.5 on 2021-03-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orders_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default='s', max_length=50, verbose_name='city'),
            preserve_default=False,
        ),
    ]