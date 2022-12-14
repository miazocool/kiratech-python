# Generated by Django 4.1.2 on 2022-10-29 03:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_remove_inventory_supplier_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkmodel',
            old_name='inventory_id',
            new_name='inventory',
        ),
        migrations.RenameField(
            model_name='linkmodel',
            old_name='supplier_id',
            new_name='supplier',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 11, 36, 4, 191825)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 11, 36, 4, 218541)),
        ),
    ]
