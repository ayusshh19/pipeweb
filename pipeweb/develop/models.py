from email.mime import image
from itertools import product
from django.db import models

# Create your models here.
class products(models.Model):
    product=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    desc=models.CharField(max_length=255)
    price=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    
class image(models.Model):
    imagepath=models.FileField(upload_to='develop/static/images/images',default='')