# Generated by Django 4.1 on 2022-08-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0009_rename_items_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='develop/static/images/images'),
        ),
    ]
