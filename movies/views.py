from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .forms import MovieForm




class HomeView(TemplateView):
    template_name = 'movies/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'movies/home.html')

home = HomeView.as_view()


class UploadView(TemplateView):
    template_name = 'movies/upload.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': MovieForm,
        }
        return render(request, 'movies/upload.html', context)

    def post(self, request, *args, **kwargs):
        form = MovieForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.save()
        return redirect(to='movies:home')


upload = UploadView.as_view()
