from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view,  name=('login')),
    path('login-lv/', views.MyLoginView.as_view(),  name=('login-lv')),

]