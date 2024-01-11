from django import forms

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price'
        ]


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            'img',
        ]
