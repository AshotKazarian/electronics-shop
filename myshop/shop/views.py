from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand

def product_list(request, category_slug=None, brand_slug=None):
    category = None
    brand = None
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'brand': brand,  # Add 'brand' to context
                   'brands': brands,  # Add 'brands' to context
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'shop/product/detail.html',
                  {'product': product})

