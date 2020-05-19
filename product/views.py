from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
     products = Product.objects.all()
     paginator = Paginator(products, 8)
     page_number = request.GET.get('page')
     product_list = paginator.get_page(page_number)
     context = {
          'product_list':product_list,
     }
     return render(request, 'product/product_list.html', context)


def product_detail(request, slug):
     # product = Product.objects.get(PRDSlug=slug)
     product = get_object_or_404(Product,PRDSlug=slug)
     context = {
          'product':product,
     }
     return render(request, 'product/product_detail.html', context)

def checkout(request):
     context = {
               
     }
     return render(request, 'product/check_out.html',context)