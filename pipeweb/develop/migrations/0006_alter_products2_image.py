# Generated by Django 4.1 on 2022-08-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0005_rename_products_products2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products2',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]