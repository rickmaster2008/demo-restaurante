from django.db import models
from www.models import Customer

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    data = models.TextField(blank=True, null=True)