from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class ChoiceType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='choice_types')
    name = models.CharField(max_length=100)
    is_multiple = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Choice(models.Model):
    choice_type = models.ForeignKey(ChoiceType, on_delete=models.CASCADE, related_name='choices')
    name = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    states = [('pr', 'Procesando'), ('co', 'Completado'), ('ca', 'Cancelado')]
    date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=2, choices=states, default='pr')
    total = models.FloatField()

    def __str__(self):
        return '#' + str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    sku = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class OrderItemChoice(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='order_item_choices')
    name = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

