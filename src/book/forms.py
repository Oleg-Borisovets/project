from django import forms
from . import models

class CityForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields=('author_name',  'author_description')
    
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


class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=( 'name', 'pic', 'price', 'binding', 'format', 'isbn', 'pages', 'the_weight', 'age_restrictions',
        'amount', 'rating', 'author','series','genres','publisher','year_edition','active') 
    
class SearchForm(forms.Form):
    q = forms.CharField(label="")
    field = forms.CharField(widget=forms.HiddenInput)
    direction = forms.CharField(widget=forms.HiddenInput)

class Home(forms.Form):
    pass

