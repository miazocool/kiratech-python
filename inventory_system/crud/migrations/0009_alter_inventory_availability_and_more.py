# Generated by Django 4.1.2 on 2022-10-29 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_alter_inventory_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='availability',
            field=models.BooleanField(verbose_name='Availability'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 18, 30, 31, 43221)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 18, 30, 31, 18144)),
        ),
    ]