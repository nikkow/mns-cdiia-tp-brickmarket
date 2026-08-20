from django.urls import path
# from .views import add, remove, ...
from . import views

# {% url 'cart:add' %}
app_name = "cart"

urlpatterns = [
  path("", views.view_cart, name="view"),
  path("add/", views.add, name="add"),
  path("set_quantity/", views.set_quantity, name="set_quantity"),
  path("remove/", views.remove, name="remove"),
  path("empty/", views.empty, name="empty")
]