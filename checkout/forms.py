from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    DELIVERY_METHOD_CHOICES = (
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    )

    delivery_method = forms.ChoiceField(
        choices=DELIVERY_METHOD_CHOICES,
        widget=forms.RadioSelect,
        initial='delivery',
        label=False,
    )

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'state', 'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'state': 'State',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'delivery_method':
                continue
            if self.fields[field].required:
                placeholder = f'{placeholders.get(field, field)} *'
            else:
                placeholder = placeholders.get(field, field)
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

    def clean(self):
        cleaned_data = super().clean()
        delivery_method = cleaned_data.get('delivery_method')

        # Validate address fields if delivery is selected
        if delivery_method == 'delivery':
            required_fields = ['postcode', 'town_or_city', 'street_address1']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(
                        field,
                        'This field is required for delivery.'
                    )
        return cleaned_data
