from django import forms
from product.models import Product,Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'status']



class ExcelForm(forms.Form):
    file = forms.FileField(label='Select an Excel file')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','discount', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        
        if self.initial.get('product'):
            self.fields['product'].widget.attrs['readonly'] = True
