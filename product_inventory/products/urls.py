from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products, name='get_products'),
    path('products/<int:product_id>/', views.get_product, name='get_product'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/update/<int:product_id>/', views.update_product, name='update_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
