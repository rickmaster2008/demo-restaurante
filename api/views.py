from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from www import models
from . import serializers

from .cart.views import CartView


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CartView(generics.RetrieveUpdateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer


class CustomerView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, req, *args, **kwargs):
        customer = models.Customer.objects.get(user=req.user)
        return Response(serializers.CustomerSerializer(instance=customer).data)
