from django import forms
from .models import Inventory, Supplier


class InventoryForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Search name', 'class': 'form-control'}))

    class Meta:
        model=Inventory
        exclude=("date_created", )

class SupplierForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Please put name', 'class': 'form-control'}))
        
    class Meta:
        model=Supplier
        exclude=("date_created", )