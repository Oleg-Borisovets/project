from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, RedirectView
from book import models as book_models
from cart import models
from . import utils
# Create your views here.
class UpdateCart(DetailView):
    model = models.Cart
    template_name = 'cart/add-book.html'
    def get_object(self, *args, **kwargs):
        print((self.request.GET), "TOKEN FOR EYES!!!")
        book_id = self.request.GET.get('book')# запрос то что собираются добавить 
        if not book_id:
            current_cart_pk = self.request.session.get('current_cart_pk')# проверяем наличие карзины в сесии 
            if current_cart_pk:
                current_cart = models.Cart.objects.filter(pk=current_cart_pk).first()
                return current_cart or []
            return []    
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')#проверка есть ли активная карзинка 
            current_customer = self.request.user
            if current_customer.is_anonymous: # проверка на анонимнасть 
                current_customer = None
            current_cart, cart_created = models.Cart.objects.get_or_create( # по добытаму id создаем карзинку или получить имеющуюся 
                pk= current_cart_pk,
                defaults={'customer': current_customer}
            )
            if cart_created:# если пришлось создать сохраняю id карзинки в сесии 
                self.request.session['current_cart_pk'] = current_cart.pk
            book =  book_models.Book.objects.get(pk=book_id)   # достаю из базы данных товар который собираюсь добавит 
            book_in_cart, book_created = models.BookInCart.objects.get_or_create(# добовление товара 
                cart = current_cart,
                book = book,
                defaults={'quantity': 1, 'price': book.price}
            )
            # if not cart_created:# проверка что если тавар уже в карзинке (если товар есть приболяем 1 к количеству)
            #     book_in_cart.quantity += 1
            #     book_in_cart.save()
        return current_cart

class RecalculateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk = self.request.session.get('current_cart_pk')
        if not current_cart_pk:
            return reverse("cart:add-to-cart")
        cart_items = self.request.GET
        utils.update_items_in_cart(cart_items, current_cart_pk)
        return reverse("cart:add-to-cart")