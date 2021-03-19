from django.urls import path
from . import views



app_name = 'orders'
urlpatterns = [
    path('orders/', views.OrdersList.as_view(), name='orders'),
    path('orders-detail/<int:pk>/', views.OrdersDetail.as_view(), name=('orders-detail')),
    path('orders-create/', views.OrdersCreate.as_view(), name='orders-create'),
    path('orders-delete/<int:pk>/', views.OrdersDelete.as_view(), name='orders-delete'),
    path('orders-update/<int:pk>/', views.OrdersUpdate.as_view(), name='orders-update'),
    path('information-order/', views.InformationOrderList.as_view(), name='information-order'),
]
