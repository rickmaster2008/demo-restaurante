from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from www import models
from . import serializers

class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer