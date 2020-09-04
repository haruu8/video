from django.urls import path
from .views import HomeView, UploadView, DetailView

app_name = 'movies'



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
]