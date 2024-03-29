from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # coerce used to convert the input to integer
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    # overriding mean create new amount for the product
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
