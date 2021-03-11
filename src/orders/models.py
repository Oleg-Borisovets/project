from django.db import models

class Orders(models.Model):
    cart = models.OneToOneField(
        "cart.Cart",
        verbose_name="Cart",
        on_delete=models.PROTECT)
    address = models.TextField("Address")
    #телефон 
    #статус
    #посмотреть в тз и добавить то что нужно 
    def __str__(self):
        return f"order #{self.pk}"