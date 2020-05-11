from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.TextField()