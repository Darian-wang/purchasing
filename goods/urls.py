from django.urls import path
from .views import index, search, add


urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('add/', add, name='add')
]