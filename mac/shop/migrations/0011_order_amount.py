# Generated by Django 4.0.2 on 2022-04-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.CharField(default='', max_length=10),
        ),
    ]
