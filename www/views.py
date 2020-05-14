from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms

@login_required(login_url='/login')
def home(req):
    return render(req, 'www/home.html')



def categories(req):
    form = forms.CategoryForm()
    context = {
        'categories': models.Category.objects.all(),
        'form': form
    }
    if req.method == 'GET':
        return render(req, 'www/categories.html', context)
    elif req.method == 'POST':
        form = forms.CategoryForm(req.POST, req.FILES)
        if form.is_valid():
            category = form.save()
            context['category'] =  category
        return render(req, 'www/categories.html', context)

def category_detail(req, id):
    category = models.Category.objects.get(pk=id)
    if req.method == 'POST':
        form = forms.CategoryForm(req.POST, req.FILES, instance=category)
        if form.is_valid():
            form.save()
        return redirect('categories')
    else:
        form = forms.CategoryForm(instance=category)
        context = {
            'category': category,
            'form': form,
        }
        return render(req, 'www/category_detail.html', context)

def category_delete(req, id):
    category = models.Category.objects.get(pk=id)
    category.delete()
    return redirect('categories')



def products(req):
    form = forms.ProductForm()
    context = {
        'products': models.Product.objects.all(),
        'categories': models.Category.objects.all(),
        'form': form,
    }
    if req.method == 'GET':
        return render(req, 'www/products.html', context)
    elif req.method == 'POST':
        form = forms.ProductForm(req.POST, req.FILES)
        if form.is_valid():
            product = form.save()
            context['product'] = product
        return render(req, 'www/products.html', context)

def product_detail(req, id):
    product = models.Product.objects.get(pk=id)
    if req.method == 'POST':
        form = forms.ProductForm(req.POST or None, instance=product)
        if form.is_valid():
            form.save()
        return redirect('products')
    elif req.method == 'GET':
        form = forms.ProductForm(instance=product)
        context = {
            'product': product,
            'form': form
        }
        return render(req, 'www/product_detail.html', context)

def product_delete(req, id):
    product = models.Product.objects.get(pk=id)
    product.delete()
    return redirect('products')


def extra_types(req):
    form = forms.ChoiceTypeForm()
    choice_types = models.ChoiceType.objects.all()
    context = {
        'form': form,
        'choice_types': choice_types,
    }
    if req.method == 'GET':
        return render(req, 'www/extra_types.html', context)
    elif req.method == 'POST':
        form = forms.ChoiceTypeForm(req.POST)
        if form.is_valid():
            choice_type = form.save()
            context['choice_type'] = choice_type
        return render(req, 'www/extra_types.html', context)

def extra_type_detail(req, id):
    extra_type = models.ChoiceType.objects.get(pk=id)
    if req.method == 'POST':
        form = forms.ChoiceTypeForm(req.POST or None, instance=extra_type)
        if form.is_valid():
            form.save()
        return redirect('extra_types')
    else:
        form = forms.ChoiceTypeForm(instance=extra_type)
        context = {
            'form': form,
            'choice_type': extra_type
        }
        return render(req, 'www/extra_type_detail.html', context)


def extra_type_delete(req, id):
    extra_type = models.ChoiceType.objects.get(pk=id)
    extra_type.delete()
    return redirect('extra-types')
        


def extras(req):
    form = forms.ChoiceForm()
    choices = models.ChoiceType.objects.all().prefetch_related('choices')
    context = {
        'choices': choices,
        'form': form
    }
    if req.method == 'GET':
        return render(req, 'www/extras.html', context)
    elif req.method == 'POST':
        form = forms.ChoiceForm(req.POST)
        if form.is_valid():
            choice = form.save()
            context['choice'] = choice
        return render(req, 'www/extras.html', context)

def extra_detail(req, id):
    extra = models.Choice.objects.get(pk=id)
    if req.method == 'POST':
        form = forms.ChoiceForm(req.POST or None, instance=extra)
        if form.is_valid():
            form.save()
        return redirect('extras')
    else:
        form = forms.ChoiceForm(instance=extra)
        context = {
            'form': form,
            'choice': extra
        }
        return render(req, 'www/extra_detail.html', context)

def extra_delete(req, id):
    extra = models.Choice.objects.get(pk=id)
    extra.delete()
    return redirect('extras')


def orders(req):
    orders = models.Order.objects.all()
    context = {
        'orders': orders
    }
    return render(req, 'www/orders/orders.html', context)

def order_detail(req, id):
    order = models.Order.objects.get(pk=id)
    context = {
        'order': order,
    }
    return render(req, 'www/orders/order_detail.html', context)

class CustomerListView(ListView):
    model = models.Customer
    template_name = 'www/customers/customers.html'
    context_object_name = 'customers'

class CustomerDeleteView(DeleteView):
    model = models.Customer
    success_url = reverse_lazy('customers')
    