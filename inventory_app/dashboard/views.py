from django.shortcuts import render
from django.http import HttpResponse
from .addProduct import ProductForm
from .models import Product
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def add(request):
    form = ProductForm
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addProduct.html', {'form':form, 'submitted':submitted})

def product_list(request):
    return render(request)

def list(request):
        product_list = Product.objects.all()
        return render(request,'listAll.html',
        {'event_list' : product_list})

def list_Sort(request):
        product_list = Product.objects.all().order_by('expiry_date')
        return render(request,'sort.html',
        {'event_list' : product_list})

