# Generated by Django 4.0.2 on 2022-03-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prodPrice',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product2',
            name='prodPrice',
            field=models.CharField(max_length=20),
        ),
    ]
