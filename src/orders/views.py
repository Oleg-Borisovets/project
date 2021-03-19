from django.shortcuts import render
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, CreateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from orders import models
from orders.models import Orders, InformationOrder
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from cart.models import Cart, BookInCart
from book.models import Book
from . import forms

# Create your views here.
class OrdersList(LoginRequiredMixin, ListView):
    model = Orders 
    template_name = 'orders/orders_list.html'
    login_url = '/accs/login-lv/'
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["сart"]= BookInCart.objects.all()
        context["pk"]= self.request.session.get('cart')
        return context

    def get_queryset(self):
        q = self.request.GET.get('q') 
        qs = super().get_queryset()
        if q:
           qs = qs.filter(name__icontains=q) # что бы искала еще ко какому нибудь полю нужон написать это так  qs = qs.filter(Q('name__icontains=q') | знак озночает или Q('имя поля по которому искать__icontains=q'))
        return qs

      

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Book"
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        q = self.request.GET.get('q') 
        context['search_form'] = forms.SearchForm(
            initial={
                'q': q,
                'field': field_to_sort_on,
                'direction': direction_to_sort_on, 
            })
        context['field_to_sort_on'] = field_to_sort_on
        context['direction_to_sort_on'] = direction_to_sort_on
        return context    

 
class OrdersDetail(LoginRequiredMixin, DetailView):
    model=Orders
    login_url = '/accs/login-lv/'
       
    

class OrdersDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('orders:orders')
    model=Orders  
    login_url = '/accs/login-lv/' 

class OrdersCreate(LoginRequiredMixin, CreateView):
    success_url=reverse_lazy('orders:information-order')
    model = Orders
    fields=('cart', 'name', 'city', 'addres', 'telephone', 'active', 'email', 'description')    
    login_url = '/accs/login-lv/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # cart_pk = self.request.session.get('cart')
        context["сart"]= BookInCart.objects.all()
        # context["pk"]= self.request.session.get('cart')
        # context["cart_pk"]= Cart.objects.all()
        # self.cart.save()
        return context
    def total_summ(self):
        all_book = self.book.all()
        total = 0
        for book in all_book:
            total += book.total_price
        return total
    
class OrdersUpdate(LoginRequiredMixin, UpdateView): 
    model=Orders
    success_url=reverse_lazy('orders:orders')
    fields=( 'cart', 'name', 'city', 'addres', 'telephone', 'active', 'email', 'description') 
    login_url = '/accs/login-lv/'
    
class InformationOrderList(LoginRequiredMixin, ListView):
    model = InformationOrder 
   
    login_url = '/accs/login-lv/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_pk = self.request.session.get('cart')
        context["сart"]= BookInCart.objects.all()
        context["pk"]= self.request.session.get('cart')
        context["cart_pk"]= Cart.objects.all()
        # self.cart.save()
        return context






  



