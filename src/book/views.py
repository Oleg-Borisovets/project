from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from book.models import Author, Series, Genres, Publisher
from django.urls import reverse, reverse_lazy
from . import forms
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


#Create your views here.
def cities_list(request):
    aut = Author.objects.all()
    context = {'aut': aut}
    return render(request, template_name='home.html', context=context)

class citieslist(LoginRequiredMixin, ListView):
    model=Author 
    login_url = '/accs/login-lv/'
    
   # permission_required = ('book.add_author', 'book.delete_author')
    
  
def cities_detail(request, pk):
    aut_1 = Author.objects.get(pk=pk)
    context = {'object': aut_1}
    return render(request, template_name='detail.html', context=context) 

class CiteDetail(LoginRequiredMixin, DetailView):
    model=Author
    login_url = '/accs/login-lv/'

def city_delete(request, pk):
    aut_1 = Author.objects.get(pk=pk)
    message = f'{aut_1.pk} delete'
    aut_1.delete()
    context = {'message': message}
    return render(request, template_name='delete.html', context=context)    

class CitiesDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('cities-cbv')
   
    model=Author
    login_url = '/accs/login-lv/'
     

def city_create(request):
    context = {}
    if request.method == "POST":
        form = forms.CityForm(request.POST)
        if form.is_valid():
            
            city = form.save()
            return HttpResponseRedirect(reverse(cities_detail, kwargs={'pk':city.pk}))
        else:
            context['form'] = form
    else:
        context['form'] = forms.CityForm()          
    
    return render(request, template_name='create.html', context=context)      

class CityCreate(LoginRequiredMixin, CreateView):
    model=Author
    success_url=reverse_lazy('cities-cbv')
    fields=("Author_name", 'pic', "Author_description")
    login_url = '/accs/login-lv/'
    #form_class = forms.CityForm # можно подкинуть свою форму всесто той которая на предыдущей строке 


def city_update(request, pk):
    context = {}
    if request.method == "GET":
        city = Author.objects.get(pk=pk)
        context = {"city": city}
    elif request.method == "POST":
        Author_name = request.POST.get("Author_name")
        Author_description = request.POST.get("Author_description")
        city = Author.objects.get(pk=pk)
        city.Author_name=Author_name
        city.Author_description=Author_description
        city.save()
        return HttpResponseRedirect(reverse(cities_detail, kwargs={'pk':city.pk}))
        
    return render(request, template_name='update.html', context=context)     


class CityUpdate(LoginRequiredMixin, UpdateView):
    model=Author
    success_url=reverse_lazy('cities-cbv')
    fields=("Author_name", "Author_description")
    login_url = '/accs/login-lv/'    


class Serieslist(LoginRequiredMixin, ListView):
    model=Series
    login_url = '/accs/login-lv/'
    
class SeriesDetail(LoginRequiredMixin, DetailView):
    model=Series
    login_url = '/accs/login-lv/'

class SeriesDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('series-cbv')
    model=Series    
    login_url = '/accs/login-lv/'

class SeriesCreate(LoginRequiredMixin, CreateView):
    model=Series
    success_url=reverse_lazy('series-cbv')
    fields=("series", "series_description")   
    login_url = '/accs/login-lv/' 

class SeriesUpdate(LoginRequiredMixin, UpdateView):
    model=Series
    success_url=reverse_lazy('series-cbv')
    fields=("series", "series_description")  
    login_url = '/accs/login-lv/'    


class Genreslist(LoginRequiredMixin, ListView):
    model=Genres
    login_url = '/accs/login-lv/'
    
class GenresDetail(LoginRequiredMixin, DetailView):
    model=Genres  
    login_url = '/accs/login-lv/'  

class GenresDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('genres-cbv')
    model=Genres    
    login_url = '/accs/login-lv/'

class GenresCreate(LoginRequiredMixin, CreateView):
    model=Genres
    success_url=reverse_lazy('genres-cbv')
    fields=("genres", "genres_description")
    login_url = '/accs/login-lv/'    

class GenresUpdate(LoginRequiredMixin, UpdateView):
    model=Genres
    success_url=reverse_lazy('genres-cbv')
    fields=("genres", "genres_description")
    login_url = '/accs/login-lv/' 


class Publisherlist(LoginRequiredMixin, ListView):
    model=Publisher
    login_url = '/accs/login-lv/'
    
class PublisherDetail(LoginRequiredMixin, DetailView):
    model=Publisher    
    login_url = '/accs/login-lv/'

class PublisherDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('publisher-cbv')
    model=Publisher   
    login_url = '/accs/login-lv/' 

class PublisherCreate(LoginRequiredMixin, CreateView):
    model=Publisher
    success_url=reverse_lazy('publisher-cbv')
    fields=("publisher", "publisher_description")    
    login_url = '/accs/login-lv/'

class PublisherUpdate(LoginRequiredMixin, UpdateView): 
    model=Publisher
    success_url=reverse_lazy('publisher-cbv')
    fields=("publisher", "publisher_description") 
    login_url = '/accs/login-lv/'

#домашняя страница 
def home_page(request):
    return render(request, template_name="home_page.html")

# Страничка менеджера 
@login_required(login_url='/accs/login-lv/')
def manager(request):
    return render(request, template_name="manager.html")

