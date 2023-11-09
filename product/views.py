from django.shortcuts import render, redirect

from .forms import ProductForm

from django.views.generic import (
    ListView,
    View,
    DetailView,
    DeleteView,
    UpdateView
)

from .models import Product


class ListProductView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'list_product': products
        }
        return render(request, 'index.html', context)


class ProductDetaileView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs.get('pk'))
        context = {
            'product': product,
            'product_name': product.name
        }
        return render(request, 'product_detail.html', context)


class DeleteProductView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'product_delete.html')

    def post(self, request, *args, **kwargs):
        Product.objects.get(id=kwargs.get('pk')).delete()
        return redirect('home')


class UpdeteProductView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product_form = ProductForm(
            initial={
                'name': product.name,
                'description': product.description,
                'price': product.price
            }
        )
        context = {
            'form': product_form,
            'product': product
        }
        return render(request, 'product_update.html', context)
    
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product.name = product_form.cleaned_data['name']
            product.description = product_form.cleaned_data['description']
            product.price = product_form.cleaned_data['price']
            product.save()
            return redirect('home')


class CreateProduct(View):
    def get(self, request):
        product_form = ProductForm()
        context = {
            'form': product_form
        }
        return render(request, 'create_product.html', context)

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
