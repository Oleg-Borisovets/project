from django.db import models

class Orders(models.Model):
    cart = models.OneToOneField(
        "cart.Cart",
        verbose_name="Cart",
        on_delete=models.PROTECT,
        )
    name = models.CharField(
        verbose_name="name", 
        max_length=50) 
        # горад
    city = models.CharField(
        verbose_name="city", 
        max_length=50)       
    
    addres = models.CharField(
        verbose_name="addres", 
        max_length=50)
    # #телефон
    telephone = models.CharField(
        verbose_name="telephone",
        max_length=50)
      # Активный (активен ли заказ, Да/Нет)
    active = models.BooleanField(
        verbose_name="Active")
    email = models.CharField(
        verbose_name="email", 
        max_length=50,
        null=True,
        blank=True)         
     
        # комментарии к заказу
    description = models.TextField(
        verbose_name= "description",
        null=True,
        blank=True)
     
    def __str__(self):
        return f"order #{self.pk}"

    @property
    def total_summ(self):
        all_book = self.book.all()
        total = 0
        for book in all_book:
            total += book.total_price
        return total    

class InformationOrder(models.Model):
    pass        