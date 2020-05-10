from django.db import models

class Order(models.Model):
    states = [('pr', 'Procesando'), ('co', 'Completado'), ('ca', 'Cancelado')]
    date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=2, choices=states, default='pr')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    interior = models.CharField(max_length=10, blank=True, null=True)
    notes = models.TextField(max_length=300, blank=True, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return '#' + str(self.pk)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    sku = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    total_price = models.DecimalField(decimal_places=2, max_digits=7)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class OrderItemChoice(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='order_item_choices')
    name = models.CharField(max_length=100)
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name