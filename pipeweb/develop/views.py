from django.shortcuts import render
from develop.models import products
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# for generating pdf invoice
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
import datetime


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generatepdf(request,id):
        try:
            order_db = products.objects.get(id = id)     #you can filter using order_id as well
        except:
            return HttpResponse("505 Not Found")

        data = {
            'order_id': order_db.id,
            'product': order_db.product,
            'date': str(datetime.date.today()),
            'size': order_db.size,
            'desc': order_db.desc,
            'price': order_db.price,
        }
        pdf = render_to_pdf('pdf.html', data)
        #return HttpResponse(pdf, content_type='application/pdf')

        # force download
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Qoutation_%s.pdf" %(data['order_id'])
            content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

PRODUCTS_PER_PAGE = 30
def test(request):
    return render(request,'pdf.html')
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