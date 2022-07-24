from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')