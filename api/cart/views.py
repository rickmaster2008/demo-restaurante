from rest_framework import viewsets
from www import models
from .serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = CartSerializer
