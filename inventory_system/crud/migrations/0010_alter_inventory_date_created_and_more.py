# Generated by Django 4.1.2 on 2022-10-29 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_alter_inventory_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 18, 54, 24, 453657)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 18, 54, 24, 428328)),
        ),
    ]
