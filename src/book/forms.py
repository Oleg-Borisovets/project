from django import forms
from . import models

class CityForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields=('Author_name', 'Author_description')
    

    #
    #
    #
    #
    #
    