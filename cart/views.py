from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from catalog.models import Product
from .cart import Cart

# Implémenter un call : /cart/add
def add(request): 
  """
  Vue pour ajouter un set au panier.
  On l'appellera uniquement en POST, avec le slug en paramètre
  """
  product_slug = request.POST.get("slug", "")
  product = get_object_or_404(
    Product, 
    slug=product_slug, status=Product.Status.AVAILABLE
  )
  cart = Cart(request)
  cart.add(product)

  next_url = request.POST.get("next")

  if next_url and url_has_allowed_host_and_scheme(
    url=next_url,
    allowed_hosts=[request.get_host()],
    require_https=request.is_secure()
  ):
    return redirect(next_url)

  return redirect('home') # TODO: Rediriger vers le panier quand il sera dispo.

def set_quantity(request):
  """
  Répondre à la demande de modification de quantité, puis rediriger
  l'utilisateur vers le panier. 
  """
  product_slug = request.POST.get("slug", "")
  product = get_object_or_404(
    Product, 
    slug=product_slug, status=Product.Status.AVAILABLE
  )

  quantity = request.POST.get("quantity", "0")
  if not quantity.isdigit():
    return redirect("cart:view")
  quantity = int(quantity)

  cart = Cart(request)
  cart.set_quantity(product, quantity)

  messages.success(request, "Quantité modifiée")

  return redirect("cart:view")

def remove(request):
  """
  Supprimer un article du panier
  """
  product_slug = request.POST.get("slug", "")
  product = get_object_or_404(
    Product, slug=product_slug
  )

  cart = Cart(request)
  cart.remove(product)
  
  messages.success(request, f"L'article {product.name} a été supprimé du panier")
  
  return redirect("cart:view")

def empty(request):
  """
  Supprimer l'ensemble des articles du panier
  """
  cart = Cart(request)
  cart.empty()
  
  messages.success(request, f"Le panier a été vidé.")
  
  return redirect("cart:view")

def view_cart(request):
  return render(request, "cart/view.html")