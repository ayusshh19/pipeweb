from django.contrib import admin
from django.urls import include, path
from .views import category, filterproduct, generatepdf, home,product,test,productlist,searchproduct

urlpatterns = [
    path('',home,name='home'),
    path('product/',product,name='product'),
    path('filter/<str:filt>',filterproduct,name='filter'),
    path('category/<str:categ>',category,name='category'),
    path('pdf/<int:id>',generatepdf,name='pdf'),
    path('productlist/',productlist,name='productlist'),
    path('searchproduct/',searchproduct,name='search')
]
