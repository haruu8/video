from django import forms
from .models import MovieContent, Comment


class MovieForm(forms.ModelForm):

    class Meta():
        model = MovieContent
        fields = ('title', 'discription', 'movie', )


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('text',)