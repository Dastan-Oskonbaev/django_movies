from django.db.models import Q
from django.http import request, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

import movie
from .forms import ReviewForm
from .models import Movie, Category, Actor, Genre


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_year(self):
        return Movie.objects.filter(draft=False).values('year')


class MovieView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movie_movies.html"


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = "url"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    model = Actor
    template_name = 'movie/actor.html'
    slug_field = 'name'


class FilterMoviesView(GenreYear, ListView):

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset


class JsonFilterMoviesView(ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        ).distinct().value('title', 'tagline', 'url', 'poster')
        return queryset

    def get(self, request, *args, **kwargs):
        queryset= list(self.get_queryset())
        return JsonResponse({'movies': queryset}, safe=False)

