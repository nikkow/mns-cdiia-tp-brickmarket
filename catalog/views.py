from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category

def product_list(request):
  products = Product.objects.all()
  categories = Category.objects.all()

  context = {
    "products": products,
    "categories": categories,
  }
  
  return render(request, "catalog/product_list.html", context)

def product(request, slug:str): 
  product = get_object_or_404(Product, slug=slug)

  context = {
    "page_title": "BrickMarket - Lego Super Store",
    "user_name": "Nicolas",
    "product": product
  }

  return render(request, "catalog/product.html", context)