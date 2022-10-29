# Generated by Django 4.1.2 on 2022-10-29 17:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_inventory_supplier_alter_inventory_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 1, 45, 58, 719613)),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='api.supplier'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 1, 45, 58, 719613)),
        ),
    ]