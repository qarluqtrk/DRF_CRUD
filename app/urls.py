from django.urls import path

from app.views import product_list, add_product, delete_product, product, update_product

urlpatterns = [
    path('', product_list, name='products'),
    path('add-product', add_product, name='add-product'),
    path('delete-product/<int:product_id>', delete_product, name='delete-product'),
    path('product/<int:product_id>', product, name='product'),
    path('update-product/<int:product_id>', update_product, name='update-product')
]