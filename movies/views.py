from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic



class HomeView(TemplateView):
    template_name = 'movies/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'movies/home.html')


