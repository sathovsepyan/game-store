from django import forms

from orders.models import Order


class CreateOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = ['game', 'user', 'total_amount']
        for field in fields:
            # self.fields[field].disabled = True
            self.fields[field].widget.attrs = {
                'class': 'form-class'
            }

    class Meta:
        model = Order
        fields = [
            'user', 'total_amount', 'game'
        ]
