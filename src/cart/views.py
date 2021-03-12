from django.shortcuts import render
from django.views.generic import DetailView
from book import models as book_models
from cart import models
# Create your views here.
class UpdateCart(DetailView):
    model = models.Cart
    template_name = 'cart/add-book.html'
    def get_object(self, *args, **kwargs):
        book_id = self.request.GET.get('book')
        if not book_id:
            pass
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
            current_customer = self.request.user
            if current_customer.is_anonymous:
                current_customer = None
            current_cart, cart_created = models.Cart.objects.get_or_create(
                pk= current_cart_pk,
                defaults={'customer': current_customer}
            )
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
                self.request.session['current_cart_pk']
            book =  book_models.Book.objects.get(pk=book_id)   
            book_in_cart, book_created = models.BookInCart.objects.get_or_create(
                cart = current_cart,
                book = book,
                defaults={'quantity': 1, 'price': book.price}
            )
            if not cart_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return current_cart