from django import forms
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(attrs={'class': 'tower-file-input'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de producto', 'rows': '5'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio', 'id': 'basic-addon2'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
        }


class ChoiceTypeForm(forms.ModelForm):
    class Meta:
        model = models.ChoiceType
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tipo de adicional'}),
            'is_multiple': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = models.Choice
        fields = '__all__'
        widgets = {
            'choice_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tipo de adicional'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'chosen': forms.CheckboxInput(attrs={'class': 'custom-control-input'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de categoría'}),
            'image': forms.FileInput(attrs={'class': 'tower-file-input'}),
        }
