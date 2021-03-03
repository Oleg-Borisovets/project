from django.contrib import admin
from . import models
from .models import Author, Series, Genres, Publisher, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'author_name',
        'author_description'
    ]

class SeriesAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'series',
        'series_description'
    ]    

class GenresAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'genres',
        'genres_description'
    ]       

class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'publisher',
        'publisher_description'
    ] 

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'pic',
        'price',
        'binding',
        'format',
        'isbn',
        'pages',
        'the_weight',
        'age_restrictions',
        'amount',
        'rating',
        'author',
        'series',
        'genres',
        'publisher',
        'created',
        'update',
        'year_edition',
        'active'
        
        
        
    ] 


admin.site.register(Author, AuthorAdmin )
admin.site.register(Series, SeriesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)


