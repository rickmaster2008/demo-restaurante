from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product_detail, name='product-detail'),
    path('products/<int:id>/delete/', views.product_delete, name="product-delete"),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:id>/', views.category_detail, name='category-detail'),
    path('categories/<int:id>/delete/', views.category_delete, name='category-delete'),
    path('extras/', views.extras, name='extras'),
    path('extras/<int:id>/', views.extra_detail, name='extra-detail'),
    path('extras/<int:id>/delete', views.extra_delete, name='extra-delete'),
    path('extra-types/', views.extra_types, name='extra-types'),
    path('extras-types/<int:id>/', views.extra_type_detail, name='extra-type-detail'),
    path('extras-types/<int:id>/delete', views.extra_type_delete, name='extra-type-delete'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:id>/', views.order_detail, name='order-detail'),
]
