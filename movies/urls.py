from django.urls import path
from .views import HomeView, UploadView

app_name = 'movies'



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadView.as_view(), name='upload'),
]