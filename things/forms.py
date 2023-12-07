"""Forms of the project."""

# Create your forms here.

from django import forms
from .models import Thing
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    description = forms.Textarea()
    quantity = forms.IntegerField(widget=forms.NumberInput)

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 0:
            raise forms.ValidationError('Quantity must be a non-negative number.')
        return quantity
