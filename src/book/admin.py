from django.contrib import admin
from . import models
from .models import Author, Series, Genres, Publisher, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'Author_name',
        'Author_description'
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
        'Price',
        'Author',      
    ] 

admin.site.register(Author, AuthorAdmin )
admin.site.register(Series, SeriesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)

