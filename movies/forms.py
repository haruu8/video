from django import forms
from .models import MovieContent


class MovieForm(forms.ModelForm):

    class Meta():
        model = MovieContent
        fields = ('title', 'discription', 'movie', )