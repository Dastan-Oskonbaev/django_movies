from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie


class MovieViews(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movie/movie_list.html", {'movie_list': movies})
