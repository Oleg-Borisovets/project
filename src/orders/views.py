from django.shortcuts import render
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, CreateView, DeleteView
from orders import models
from orders.models import Orders


# Create your views here.
class Orders(ListView):
    model = Orders 
    template_name = 'orders/orders_list.html'
