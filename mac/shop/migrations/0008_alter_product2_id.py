# Generated by Django 4.0.2 on 2022-04-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_order_id_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product2',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
