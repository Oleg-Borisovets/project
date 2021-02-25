from django import forms
from . import models

class CityForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields=('Author_name', 'pic', 'Author_description')
    
class CityForm(forms.ModelForm):
    class Meta:
        model=models.Series
        fields=('series',  'series_description')    

class CityForm(forms.ModelForm):
    class Meta:
        model=models.Genres
        fields=('genres',  'genres_description')   

class CityForm(forms.ModelForm):
    class Meta:
        model=models.Publisher
        fields=('publisher',  'publisher_description')                 

    
    