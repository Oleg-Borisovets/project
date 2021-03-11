from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=False,
        null=True
    )
    def __str__(self):
        return f"cart #{self.pk}"
    

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name= "Cart",
        related_name="book",
        on_delete=models.CASCADE)
    book = models.ForeignKey(
        "book.Book", verbose_name= "Book in a cart",
        on_delete=models.PROTECT)

    quantity = models.IntegerField("Quantity", default=1)
    price = models.DecimalField(
        "Price", 
        max_digits=5,
        decimal_places=2)    
    def __str__(self):
        return f"BookInCart #{self.pk} {self.book.name} quantity {self.quantity}"        
