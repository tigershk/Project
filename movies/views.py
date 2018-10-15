#Added for phase2
# from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework as filters
from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

#filters defined here.

class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    imdbid = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ('title','imdbid')

# Create your views here.
class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_class = MovieFilter


# Following code requires exact match
# class MovieView(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     filter_fields = ('title','imdbid') # allows http://127.0.0.1:8000/movies/?title=&imdbid=tt0114709 or http://127.0.0.1:8000/movies/?title=Toy+Story&imdbid=

