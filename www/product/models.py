from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    in_stock = models.BooleanField(default=True)
    discount_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
    
class ChoiceType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='choice_types')
    name = models.CharField(max_length=100)
    is_multiple = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Choice(models.Model):
    choice_type = models.ForeignKey(ChoiceType, on_delete=models.CASCADE, related_name='choices')
    name = models.CharField(max_length=100)
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7)
    chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.name