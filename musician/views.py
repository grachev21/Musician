from django.shortcuts import render 
from django.views.generic.list import ListView
from .models import ProfileUser



class Home(ListView):
    template_name = 'musician/home.html'
    model = ProfileUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    



