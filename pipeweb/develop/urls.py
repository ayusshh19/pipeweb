from django.contrib import admin
from django.urls import include, path
from .views import addproduct, category, deleteprod, filterproduct, generatepdf, home, loginadmin,product,test,productlist,searchproduct,generateallpdf, updateprod,updateitem
urlpatterns = [
    path('',home,name='home'),
    path('product/',product,name='product'),
    path('filter/<str:filt>',filterproduct,name='filter'),
    path('category/<str:categ>',category,name='category'),
    path('pdf/<int:id>',generatepdf,name='pdf'),
    path('productlist/',productlist,name='productlist'),
    path('searchproduct/',searchproduct,name='search'),
    path('all/',generateallpdf,name='generateall'),
    path('adminlogin/',loginadmin,name='adminlogin'),
    path('addproduct/',addproduct,name='add'),
    path('delete/<int:id>',deleteprod,name='delete'),
    path('update/<int:id>',updateprod,name='update'),
    path('updateitem',updateitem,name='updateitem')
]
