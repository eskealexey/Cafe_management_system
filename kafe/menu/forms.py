from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput

from .models import Item


class ItemsForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','price', 'active_is']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', }),
            'price': NumberInput(attrs={'class': 'form-control', }),
            'active_is': CheckboxInput(attrs={'class': 'form-check-input','checked': 'checked' }),
        }
