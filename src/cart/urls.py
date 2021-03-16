from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add-to-cart/', views.UpdateCart.as_view(), name='add-to-cart'),
    path('recalculate-cart/', views.RecalculateCart.as_view(), name='recalculate-cart')

]
