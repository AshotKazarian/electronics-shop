from django.contrib import admin
from .models import Category, Brand, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug', 'price', 'brand', 'category', 'available', 'created', 'updated', 'get_short_description'] 
  list_filter = ['available', 'created', 'updated', 'brand', 'category']
  list_editable = ['price', 'available']
  prepopulated_fields = {'slug': ('name',)}
  list_display_links = ['name']  
  raw_id_fields = ('category',)
  readonly_fields = ('brand',)
  search_fields = ('name', 'category__name', 'brand__name', 'slug', 'price', 'description', 'updated',) 
  date_hierarchy = 'updated'
  
  def get_short_description(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
