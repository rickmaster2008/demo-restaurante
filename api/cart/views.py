from rest_framework import generics
from rest_framework.validators import ValidationError
from www import models
from .serializers import CartSerializer


class CartView(generics.RetrieveUpdateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        queryset = models.Cart.objects.get(user=request.user)
        if queryset.exists():
            raise ValidationError('no tienes un carrito aun')
