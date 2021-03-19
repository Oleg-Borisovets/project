from django import forms
from . import models



class OrdersForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=("cart",) 


class SearchForm(forms.Form):
    q = forms.CharField(label="")
    field = forms.CharField(widget=forms.HiddenInput)
    direction = forms.CharField(widget=forms.HiddenInput)        