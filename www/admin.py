from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.ChoiceType)
admin.site.register(models.Choice)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.OrderItemChoice)
admin.site.register(models.Customer)

