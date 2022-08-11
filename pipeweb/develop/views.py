from django.shortcuts import render
from develop.models import products
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

PRODUCTS_PER_PAGE = 24
# Create your views here.
def home(request):
    return render(request,'index.html')

def product(request,categ=None):
    product=products.objects.all()
    page = request.GET.get('page',1)
    product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
    try:
        product = product_paginator.page(page)
        print(product_paginator)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
    except:
        product = product_paginator.page(PRODUCTS_PER_PAGE)
    return render(request,'product.html',{"product":product, 'page_obj':product, 'is_paginated':True, 'paginator':product_paginator})


def filterproduct(request,filt):
    if filt =='assend':
        product=products.objects.all().order_by('price')
        page = request.GET.get('page',1)
        product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
        try:
            product = product_paginator.page(page)
            print(product_paginator)
        except EmptyPage:
            product = product_paginator.page(product_paginator.num_pages)
        except:
            product = product_paginator.page(PRODUCTS_PER_PAGE)
        return render(request,'product.html',{"product":product, 'page_obj':product, 'is_paginated':True, 'paginator':product_paginator})
    elif filt=='desend':
        product=products.objects.all().order_by('-price')
        page = request.GET.get('page',1)
        product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
        try:
            product = product_paginator.page(page)
            print(product_paginator)
        except EmptyPage:
            product = product_paginator.page(product_paginator.num_pages)
        except:
            product = product_paginator.page(PRODUCTS_PER_PAGE)
        return render(request,'product.html',{"product":product, 'page_obj':product, 'is_paginated':True, 'paginator':product_paginator})
    else:
        product=products.objects.all()
        page = request.GET.get('page',1)
        product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
        try:
            product = product_paginator.page(page)
            print(product_paginator)
        except EmptyPage:
            product = product_paginator.page(product_paginator.num_pages)
        except:
            product = product_paginator.page(PRODUCTS_PER_PAGE)
        return render(request,'product.html',{"product":product, 'page_obj':product, 'is_paginated':True, 'paginator':product_paginator})
        
def category(request,categ):
    product=products.objects.filter(Q(('{}__icontains'.format("desc"), categ))|Q(('{}__icontains'.format("type"), categ))).order_by('price')
    page = request.GET.get('page',1)
    product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
    try:
        product = product_paginator.page(page)
        print(product_paginator)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
    except:
        product = product_paginator.page(PRODUCTS_PER_PAGE)
    return render(request,'product.html',{"product":product, 'page_obj':product, 'is_paginated':True, 'paginator':product_paginator})