from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, CreateView, DeleteView

from book import models as book_models
from cart import models
from . import utils
from cart.models import Cart, BookInCart

# Create your views here.
class UpdateCart(DetailView):
    model = models.Cart
    template_name = 'cart/add-book.html'
    def get_object(self, *args, **kwargs):  
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
        current_cart_pk, cart_items_from_form = utils.harvest_data(self)
        if not current_cart_pk:
            return reverse("cart:add-to-cart")
        action = utils.update_items_in_cart(cart_items_from_form, current_cart_pk)   
        return reverse("cart:add-to-cart")

# class RecalculateCart(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return_urls = {
#             'checkout': reverse("cart:checkout")
#         }
#         current_cart_pk, cart_items_from_form = utils.harvest_data(self)
#         if not current_cart_pk:
#             return reverse("cart:add-to-cart")
#         action = utils.update_items_in_cart(cart_items_from_form, current_cart_pk)
#         if action == "checkout":
#             url = reverse("cart:checkout")
#         else:
#             url = reverse("cart:add-to-cart")    
#         return url        


# class Checkout(ListView):
#     model = Checkout
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["BookInCart"]= BookInCart.objects.all()
#         return context

# class Checkoutlist(ListView):
#     model=Checkout
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["BookInCart"]= BookInCart.objects.all()
#         return context
      
    
# class CheckoutDetail(LoginRequiredMixin, DetailView):
#     model=Checkout
    

# class CheckoutDelete(LoginRequiredMixin, DeleteView):
#     success_url=reverse_lazy('series-cbv')
#     model=Checkout    
    

# class CheckoutCreate(CreateView):
#     model=Checkout
#     fields=("name", "description")   
     

# class CheckoutUpdate(LoginRequiredMixin, UpdateView):
#     model=Checkout
#     success_url=reverse_lazy('series-cbv')
#     fields=("series", "series_description")  
#     login_url = '/accs/login-lv/'    



