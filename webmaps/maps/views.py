from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import App
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.template import loader

#Create your views here.
class IndexView(generic.ListView):
    template_name = 'home'
    model = App
    #For ListView, the automatically generated context variable is model_list
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return App.objects.filter(user=self.request.user)

def detail(request,app_id):
    #app = get_object_or_404(App, pk=App.id)
    if app_id == 1:
        return render(request, 'emmaapp1.html')
    elif app_id == 2:
        return render(request, 'emmaapp2.html')
    elif app_id == 3:
        return render(request, 'yiranapp1.html')
    elif app_id == 4:
        return render(request, 'yiranapp2.html')