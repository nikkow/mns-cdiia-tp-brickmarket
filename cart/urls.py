from django.urls import path
# from .views import add, remove, ...
from . import views

# {% url 'cart:add' %}
app_name = "cart"

urlpatterns = [
  path("", views.view_cart, name="view"),
  path("add/", views.add, name="add")
]