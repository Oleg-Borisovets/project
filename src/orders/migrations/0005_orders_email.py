# Generated by Django 3.1.5 on 2021-03-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orders_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.CharField(default='q', max_length=50, verbose_name='email'),
            preserve_default=False,
        ),
    ]
