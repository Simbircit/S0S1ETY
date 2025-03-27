from django.contrib.auth.urls import path
from . import views
app_name = 'catalog'

urlpatterns = [
    path('catalog/', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    path('orders/', views.order_list, name='order_list'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('add/<int:product_id>/', views.add_to_cart2, name='add_to_cart2'),
    path('remove_one/<int:item_id>/', views.remove_one_from_cart, name='remove_one_from_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart')
]
