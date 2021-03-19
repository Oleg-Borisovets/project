# Generated by Django 3.1.5 on 2021-03-19 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20210318_1005'),
        ('orders', '0014_auto_20210319_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='orders',
            name='cart',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='cart.cart', verbose_name='Cart'),
            preserve_default=False,
        ),
    ]
