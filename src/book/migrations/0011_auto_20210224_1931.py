# Generated by Django 3.1.5 on 2021-02-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20210224_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='pic',
            field=models.ImageField(upload_to='uploads/', verbose_name='Picture'),
        ),
    ]