from django.contrib import admin
from django.urls import include, path
from .views import category, filterproduct, home,product

urlpatterns = [
    path('',home,name='home'),
    path('product/',product,name='product'),
    path('filter/<str:filt>',filterproduct,name='filter'),
    path('category/<str:categ>',category,name='category'),
]
