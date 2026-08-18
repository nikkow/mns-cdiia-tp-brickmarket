from django.shortcuts import render
from django.http import HttpResponse

def product(request, id:int|None = None ): 

  context = {
    "page_title": "BrickMarket - Lego Super Store",
    "user_name": "Nicolas",
    "product": {
      "id": 10329,
      "name": "Les plantes miniatures",
      "price": 49.99,
      "category": "Botanicals",
      "short_description": "Un projet relaxant pour construire neuf petites plantes tropicales, carnivores et de climat aride, puis créer une décoration végétale sans entretien.",
      "image_url": "https://m.media-amazon.com/images/I/81wYL4wpxjL._AC_SX679_.jpg",
      "age": "18+",
      "parts": 749,
      "status": "AVAILABLE",
      "slug": "les-plantes-miniatures",
      "points": 375,
    }
  }

  return render(request, "catalog/product.html", context)