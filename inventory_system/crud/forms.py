from django import forms
from .models import Inventory, Supplier


class InventoryForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Name','class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Descrition', 'class': 'form-control'}))
    note = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Note', 'class': 'form-control'}))
    stock = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Stock', 'class': 'form-control'}))
    availability = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Availability', 'class': 'form-control'}))

    class Meta:
        model=Inventory
        exclude=("date_created", )

class SupplierForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Please put name', 'class': 'form-control'}))
        
    class Meta:
        model=Supplier
        exclude=("date_created", )