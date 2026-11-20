from django import forms
from .models import Box, InventoryItem

class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ['box_number', 'notes']
        widgets = {
            'box_number': forms.TextInput(attrs={'placeholder': 'e.g. 1 or GARAGE-01'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional notes about this box'}),
        }

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['description']
        widgets = {'description': forms.TextInput(attrs={'placeholder': 'Describe the item'})}
