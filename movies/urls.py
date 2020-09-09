from django.urls import path
from .views import HomeView, UploadView, DetailView
from .views import add_comment
from . import views

app_name = 'movies'



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
]