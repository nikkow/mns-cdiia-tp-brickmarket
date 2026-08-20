from catalog.models import Product

SHIPPING_FEES = 790 # in cents
FREE_SHIPPING_THRESHOLD = 7500 # in cents 
CART_SESSION_KEY = 'cart' # Clé du dictionnaire pour stocker le panier dans la session

class Cart:
  def __init__(self, request):
    self.session = request.session

    cart = self.session.get(CART_SESSION_KEY)
    if cart is None: 
      cart = {}
      self.session[CART_SESSION_KEY] = cart
    # Stockage cible:
    # {"<slug produit>": <quantité>}
    self.cart = cart

  def add(self, product, quantity = 1):
    """
    On ajoute un produit au panier s'il n'existe pas, 
    ou on ajuste sa quantité s'il existe déjà.
    """
    if product.slug in self.cart:
      self.cart[product.slug]["quantity"] += quantity
    else:
      self.cart[product.slug] = {"quantity": quantity}
    self.session.modified = True

  def remove(self, product): 
    """
    On supprime un produit du panier. On a recours à la 
    fonction pop() des dictionnaires pour extraire. 
    """
    self.cart.pop(product.slug, None)
    self.session.modified = True

  def set_quantity(self, product, quantity):
    if product.slug in self.cart: 
      self.cart[product.slug]["quantity"] = quantity
      if self.cart[product.slug]["quantity"] <= 0:
        self.remove(product)
    else:
      if quantity > 0:
        self.cart[product.slug] = {"quantity": quantity}
    self.session.modified = True

  def empty(self): 
    self.session[CART_SESSION_KEY] = {}
    self.session.modified = True

  def __iter__(self):
    """
    On crée un itérateur sur les produits du panier. 
    Cette fonction nous permettra d'utiliser directement "cart" dans une boucle 
    Exemple : 
    my_cart = Cart()
    my_cart.add(<un produit>)

    for item in my_cart: <= possible du fait qu'on a implémenté __iter__
    """
    products = Product.objects.filter(slug__in=self.cart.keys())
    for product in products: 
      quantity = self.cart[product.slug]["quantity"]
      yield {
        "product": product,
        "quantity": quantity,
        "total_price_in_cents": product.price * quantity
      }

  def subtotal(self): 
    """
    Calcule le sous-total du panier hors frais de livraison
    """

    # Equivalent en une seule ligne : 
    # return sum(line["total_price"] for line in self)

    total = 0
    for line in self:
      total += line["total_price_in_cents"]

    return total

  def shipping_fees(self): 
    if not self.cart or self.subtotal() >= FREE_SHIPPING_THRESHOLD:
      return 0
    else: 
      return SHIPPING_FEES

  def total(self):
    return self.subtotal() + self.shipping_fees()

  def is_shipping_free(self):
    return self.shipping_fees() == 0 and self.cart