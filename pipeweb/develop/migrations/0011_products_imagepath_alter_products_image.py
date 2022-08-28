# Generated by Django 4.1 on 2022-08-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0010_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='imagepath',
            field=models.FileField(default='', upload_to='develop/static/images/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
