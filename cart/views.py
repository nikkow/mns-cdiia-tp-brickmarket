from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import url_has_allowed_host_and_scheme
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

def view_cart(request):
  cart = Cart(request)
  return render(request, "cart/view.html", {"cart": cart})