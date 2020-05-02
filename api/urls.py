from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('categories', views.CategoryViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
] + router.urls