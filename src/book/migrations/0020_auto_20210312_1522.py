# Generated by Django 3.1.5 on 2021-03-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_auto_20210311_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]