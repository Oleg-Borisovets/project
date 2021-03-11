# Generated by Django 3.1.5 on 2021-03-10 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0002_auto_20210310_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Address')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cart.cart', verbose_name='Cart')),
            ],
        ),
    ]
