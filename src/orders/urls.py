from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
    path('orders/', views.Orders.as_view(), name='orders'),
]
