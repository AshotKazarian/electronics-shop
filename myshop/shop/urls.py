from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('brand/<slug:brand_slug>/', views.product_list, name='product_list_by_brand'), 
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

