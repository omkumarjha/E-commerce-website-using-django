# Generated by Django 4.0.2 on 2022-04-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]
