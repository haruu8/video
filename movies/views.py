from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.views import generic
from .forms import MovieForm, CommentForm
from .models import MovieContent, Comment




class HomeView(TemplateView):
    template_name = 'movies/home.html'

    def get(self, request, *args, **kwargs):
        movie_contents = MovieContent.objects.all().order_by('-created_at')
        context = {
            'movie_contents': movie_contents
        }
        return render(request, 'movies/home.html', context)

home = HomeView.as_view()


class UploadView(TemplateView):
    template_name = 'movies/upload.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': MovieForm,
        }
        return render(request, 'movies/upload.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                post.save()
                return redirect(to='movies:home')
        else:
            form = MovieForm()
        return render(request, 'movies/upload.html', {'form': form})


upload = UploadView.as_view()


class DetailView(DetailView):

    template_name = 'movies/detail.html'
    model = MovieContent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

detail = DetailView.as_view()



def add_comment(request, pk):
    movie = get_object_or_404(MovieContent, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movies:detail', pk=movie.pk)
    else:
        form = CommentForm()
    print(form)
    return render(request, 'movies/add_comment.html', {'form': form})