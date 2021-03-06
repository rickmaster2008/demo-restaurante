from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('categories', views.CategoryViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('carts/<int:pk>/', views.CartView.as_view(), name='api-cart'),
    path('register/', views.RegisterView.as_view(), name='api-register'),
    path('customer/', views.CustomerView.as_view(), name='api-customer')
] + router.urls
