# Generated by Django 3.1.5 on 2021-03-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orders_author_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
            preserve_default=False,
        ),
    ]
