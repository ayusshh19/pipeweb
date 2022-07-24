from django.contrib import admin
from django.urls import include, path
from .views import home,product

urlpatterns = [
    path('',home,name='home'),
    path('product/',product,name='product'),
]
