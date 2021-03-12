from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from book.models import Author, Series, Genres, Publisher, Book
from django.urls import reverse, reverse_lazy
from . import forms
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from book import models as book_models







#Create your views here.
# def cities_list(request):
#     aut = Author.objects.all()
#     context = {'aut': aut}
#     return render(request, template_name='home.html', context=context)

class citieslist(LoginRequiredMixin, ListView):
    model=Author 
    login_url = '/accs/login-lv/'
    paginate_by = 5
    
    
   # permission_required = ('book.add_author', 'book.delete_author')
    
  
# def cities_detail(request, pk):
#     aut_1 = Author.objects.get(pk=pk)
#     context = {'object': aut_1}
#     return render(request, template_name='detail.html', context=context) 

class CiteDetail(LoginRequiredMixin, DetailView):
    model=Author
    login_url = '/accs/login-lv/'

# def city_delete(request, pk):
#     aut_1 = Author.objects.get(pk=pk)
#     message = f'{aut_1.pk} delete'
#     aut_1.delete()
#     context = {'message': message}
#     return render(request, template_name='delete.html', context=context)    

class CitiesDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('cities-cbv')
   
    model=Author
    login_url = '/accs/login-lv/'
     

# def city_create(request):
#     context = {}
#     if request.method == "POST":
#         form = forms.CityForm(request.POST)
#         if form.is_valid():
            
#             city = form.save()
#             return HttpResponseRedirect(reverse(cities_detail, kwargs={'pk':city.pk}))
#         else:
#             context['form'] = form
#     else:
#         context['form'] = forms.CityForm()          
    
#     return render(request, template_name='create.html', context=context)      

class CityCreate(LoginRequiredMixin, CreateView):
    model=Author
    success_url=reverse_lazy('cities-cbv')
    fields=("author_name",  "author_description")
    login_url = '/accs/login-lv/'
    #form_class = forms.CityForm # можно подкинуть свою форму всесто той которая на предыдущей строке 


# def city_update(request, pk):
#     context = {}
#     if request.method == "GET":
#         city = Author.objects.get(pk=pk)
#         context = {"city": city}
#     elif request.method == "POST":
#         Author_name = request.POST.get("Author_name")
#         Author_description = request.POST.get("Author_description")
#         city = Author.objects.get(pk=pk)
#         city.Author_name=Author_name
#         city.Author_description=Author_description
#         city.save()
#         return HttpResponseRedirect(reverse(cities_detail, kwargs={'pk':city.pk}))
        
#     return render(request, template_name='update.html', context=context)     


class CityUpdate(LoginRequiredMixin, UpdateView):
    model=Author
    success_url=reverse_lazy('cities-cbv')
    fields=("author_name", "author_description")
    login_url = '/accs/login-lv/'    


class Serieslist(LoginRequiredMixin, ListView):
    model=Series
    login_url = '/accs/login-lv/'
    paginate_by = 5
    
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
    paginate_by = 5
    
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
    paginate_by = 5
    
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
# def home_page(request):
#     return render(request, template_name="home_page.html")

# class Home(ListView):
#     model=Home
    

# class Test(ListView):
#     model=Test

class Home(TemplateView):
    template_name = "home_page.html"

      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"]= Book.objects.all()
        context["book_n"]= Book.objects.all().order_by("-pk")[:5]
        context["author"]= Author.objects.all().order_by("-pk")[:5]
        return context


    









# Страничка менеджера 
@login_required(login_url='/accs/login-lv/')
def manager(request):
    return render(request, template_name="manager.html")



# class Booklist(ListView):
#     model=Book
    


class Booklist(LoginRequiredMixin, ListView):
    model=Book
    login_url = '/accs/login-lv/'
    paginate_by = 5
 # сортировка
    def get_ordering(self):
        ordering_by = "pk"
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        if field_to_sort_on and direction_to_sort_on:
            direction_dict = {'up': ""}   
            ordering_by = f'{direction_dict.get(direction_to_sort_on, "-")}{field_to_sort_on}'     
        return ordering_by

    # def get_queryset(self):
    #    return super().get_queryset()#.filter(#как сортируем) # сортировка 

# поиск
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



class BookDetail(LoginRequiredMixin, DetailView):
    model=Book   
    login_url = '/accs/login-lv/'


class BookDelete(LoginRequiredMixin, DeleteView):
    success_url=reverse_lazy('book')
    model=Book  
    login_url = '/accs/login-lv/' 

class BookCreate(LoginRequiredMixin, CreateView):
    model=Book
    success_url=reverse_lazy('book')
    fields=(  'name','price','binding','format','isbn','pages','the_weight','age_restrictions','amount','rating',
        'author','series','genres','publisher','year_edition','active','pic')    
    login_url = '/accs/login-lv/'

class BookUpdate(LoginRequiredMixin, UpdateView): 
    model=Book
    success_url=reverse_lazy('book')
    fields=(  'name','price','binding','format','isbn','pages','the_weight','age_restrictions','amount','rating',
        'author','series','genres','publisher','year_edition','active','pic') 
    login_url = '/accs/login-lv/'