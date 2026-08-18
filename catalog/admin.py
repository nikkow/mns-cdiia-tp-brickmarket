from django.contrib import admin
from .models import Category, Product

# admin.site.register(Category)
admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ["name", "slug", "product_count"]
  search_fields = ["name"]

  prepopulated_fields = {"slug": ("name", )}

  @admin.display(description="Nombre de sets")
  def product_count(self, category):
    return category.products.count()