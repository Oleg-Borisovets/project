from django.contrib import admin
from . import models

# Register your models here.



class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'cart',
        'name',
        'city',
        'address',
        'telephone',
        'active',
        'email',
        'description'
    ]



admin.site.register(models.Cart)
admin.site.register(models.BookInCart)



