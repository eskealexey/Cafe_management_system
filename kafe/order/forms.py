from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, SelectMultiple, Select

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items']
        widgets = {
            'table_number': NumberInput(attrs={'class': 'form-control', }),
            'items': SelectMultiple(attrs={'class': 'form-control', }),
            # 'status': Select(attrs={'class': 'form-control', }),
        }


class OrderStatusForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        # widgets = {
        #     'status': Select(attrs={'class': 'form-control', }),
        # }