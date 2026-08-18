from django.db import models

class Category(models.Model):
  name = models.CharField("nom", max_length=100, unique=True)
  description = models.TextField("description", blank=True)
  slug = models.SlugField("identifiant url", max_length=100, unique=True)

  class Meta:
    verbose_name = "catégorie"
    verbose_name_plural = "catégories"
    ordering = ["name"]

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField("nom", max_length=200)
  short_description = models.TextField("description courte", blank=True)
  price = models.PositiveIntegerField("Prix")
  # image_path = models.CharField("Chemin de l'image", max_length=150)
  image_url = models.URLField("Adresse complète", max_length=500)
  age = models.CharField("Age conseillé", default="18+")
  parts_count = models.PositiveIntegerField("nombre de pièces")

  # status = models.CharField("disponibilité", choices=[
  #   ("AVAILABLE", "Disponible"),
  #   ("LIMITED", "Stock limité"),
  #   ("PREORDER", "Précommande"),
  #   ("OUTOFSTOCK", "Hors stock")
  # ])

  class Status(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Disponible"
    LIMITED = "LIMITED", "Stock limité"
    PREORDER = "PREORDER", "Précommande"
    OUTOFSTOCK = "OUTOFSTOCK", "Hors stock"

  status = models.CharField("disponibilité", max_length=20, choices=Status.choices, default=Status.AVAILABLE)

  rewards_points = models.PositiveIntegerField("points de récompense", default=0)
  slug = models.SlugField("identifiant url", max_length=200, unique=True)

  category = models.ForeignKey(
    Category, 
    verbose_name="catégorie",
    on_delete=models.PROTECT,
    related_name="products"
  )

  created_at = models.DateTimeField("Créé le", auto_now_add=True)

  class Meta: 
    verbose_name = "set LEGO"
    verbose_name_plural = "sets LEGO"
    ordering = ["-created_at"]

  def __str__(self):
    return self.name