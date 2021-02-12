from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from book.models import Author
from django.urls import reverse, reverse_lazy
from . import forms
from django.views.generic import DetailView, ListView, DeleteView, CreateView
from book.models import Author

# Create your views here.
def cities_list(request):
    aut = Author.objects.all()
    context = {'aut': aut}
    return render(request, template_name='home.html', context=context)

class citieslist(ListView):
    model=Author   
  
def cities_detail(request, pk):
    aut_1 = Author.objects.get(pk=pk)
    context = {'object': aut_1}
    return render(request, template_name='detail.html', context=context) 

class CiteDetail(DetailView):
    model=Author

def city_delete(request, pk):
    aut_1 = Author.objects.get(pk=pk)
    message = f'{aut_1.pk} delete'
    aut_1.delete()
    context = {'message': message}
    return render(request, template_name='delete.html', context=context)    

class CitiesDelete(DeleteView):
    success_url=reverse_lazy('cities-cbv')
   
    model=Author
     

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

class CityCreate(CreateView):
    model=Author
    success_url=reverse_lazy('cities-cbv')
    fields=("Author_name", "Author_description")
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


    