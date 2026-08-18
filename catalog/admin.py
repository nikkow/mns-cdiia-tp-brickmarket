from django.contrib import admin
from .models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ["name", "slug", "price", "status", "category"]
  search_fields = ["name"]

  prepopulated_fields = {"slug": ("name",)}
  list_filter = ["category", "status"]
  list_editable = ["price", "status"]

  fieldsets = [
    (
      "Identité du set",
      {"fields": ["name", "slug", "category"]}
    ),
    (
      "Vente",
      {"fields": ["price", "status", "rewards_points"]}
    ),
    (
      "Caractéristiques",
      {"fields": ["parts_count", "age"]}
    ),
    (
      "Présentation",
      {"fields": ["short_description", "image_url"], "classes": ["collapse"]}
    )
  ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ["name", "slug", "product_count"]
  search_fields = ["name"]

  prepopulated_fields = {"slug": ("name", )}

  @admin.display(description="Nombre de sets")
  def product_count(self, category):
    return category.products.count()