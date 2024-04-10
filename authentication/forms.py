from django import forms
from .models import SellerProfile, Store,Product, ProductImage

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = ['face_picture', 'id_picture']
        widgets = {
            'face_picture': forms.FileInput(attrs={'accept':'image/*', 'capture':'camera'}),
            'id_picture': forms.FileInput(attrs={'accept':'image/*', 'capture':'camera'}),
        }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'location', 'store_picture']
        widgets = {
            'store_picture': forms.FileInput(attrs={'accept':'image/*', 'capture':'camera'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price','stock', 'condition', 'brand', 'model_number', 'tags','store']
        required = ['title', 'description', 'category', 'price','stock', 'condition','store']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']

