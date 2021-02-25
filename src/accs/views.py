from django.shortcuts import render
from django.urls import reverse
from . import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, views
# Create your views here.

def login_view(request):
    
    template_name='accs/login.html'
    if request.method =="GET":
        login_form = forms.LoginForm()
        return render(
            request, 
            template_name=template_name, context={"form": login_form})
    elif request.method =="POST":
        #print(request.POST)
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username= login_form.cleaned_data['username']
            password= login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) 
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('cities-cbv'))
            else:return render(
                request, 
                template_name=template_name,  context={"form": login_form})
        else:
            return render(
                request, 
                template_name=template_name, context={"form": login_form})


class MyLoginView(views.LoginView):
    template_name='accs/login.html'
