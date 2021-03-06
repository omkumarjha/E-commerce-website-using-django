# Generated by Django 4.0.2 on 2022-04-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_prodprice_alter_product2_prodprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.TextField(max_length=40)),
                ('phone', models.IntegerField()),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product2',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
