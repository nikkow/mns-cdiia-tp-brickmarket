from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category

def product_list(request):
  category_slug = request.GET.get("category", "").strip()
  products = Product.objects.all()
  categories = Category.objects.all()

  current_category = None
  if category_slug:
    current_category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=current_category)

  context = {
    "products": products,
    "categories": categories,
    "current_category": current_category
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