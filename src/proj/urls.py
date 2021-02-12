"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import cities_list
from book.views import cities_detail
from book.views import city_delete
from book.views import city_create
from book.views import city_update
from book.views import CiteDetail, citieslist, CitiesDelete  
from book import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', views.cities_list),
    path('cities-cbv/', views.citieslist.as_view(), name=('cities-cbv')),
    path('cities/<int:pk>/', views.cities_detail),
    path('cities-cbv/<int:pk>/', views.CiteDetail.as_view(), name=('cities-Detail')),
    path('city_delete/<int:pk>/', views.city_delete),
    path('city_delete-cbv/<int:pk>/', views.CitiesDelete.as_view()),
    path('city_create/', views.city_create),
    path('city_create-cbv/', views.CityCreate.as_view()),
    path('city_update/<int:pk>/', views.city_update)
    
   
]
