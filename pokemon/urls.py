# pokemon/urls.py
from django.urls import path
from . import views

app_name = 'pokemon' # This is important for namespacing URLs

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'), # Root path for the app
    path('<str:pokemon_name_or_id>/', views.pokemon_detail, name='pokemon_detail'),
]