from django.shortcuts import render
from django.http import HttpResponse
from book.models import Author


# Create your views here.
def home_page(request):
    aut = Author.objects.first()
    context = {'aut': aut}
    return render(request, template_name='home.html', context=context)
  