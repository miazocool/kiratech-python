# Generated by Django 4.1.2 on 2022-10-29 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_inventory_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 16, 43, 58, 541601)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 16, 43, 58, 541601)),
        ),
    ]