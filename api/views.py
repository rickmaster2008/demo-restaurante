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

    # def create(self, request, *args, **kwargs):
    #     order_items = request.data.pop('order_items')
    #     order_serializer = serializers.OrderSerializer(data=request.data)
    #     if order_serializer.is_valid(raise_exception=True):
    #         order_serializer.save()
    #     return super().create(request, *args, **kwargs)