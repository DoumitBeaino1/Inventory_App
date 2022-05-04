from unicodedata import name
from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name','GTIN','expiry_date')

        labels = {
            'name': '',
            'GTIN': '',
            'expiry_date': 'EXP',
        }
    
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Item_Name' }),
            'GTIN': forms.TextInput(attrs={'placeholder': 'GTIN'}),
            'expiry_date': forms.SelectDateWidget(attrs={'placeholder': 'Expiry_Date'}),
        }
    

